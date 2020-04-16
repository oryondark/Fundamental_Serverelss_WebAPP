import time
module_start = time.time()
import json
import numpy as np
import pickle
import base64
import csv
print("[BreakTime] KNN Python Dependencies Library load : ", time.time() - module_start)

from watcher import Watcher
watching = Watcher(td=True)
knn_model, _ = watching.watch(pickle.load, [open('knn_model.pkl','rb')], name='knn_model_inialization')

def reduce_v(pair):
    cache = {}
    for k, v in pair.items():
        if v not in cache.values():
            cache[k] = v
        if len(cache.values()) == 3:
            break

    return cache

def find_clothe(k_predited_data):
    trans_closest = []
    knn_match_time = time.time()
    patchs = np.load("patch_trained.npy")
    for a in range(0, len(k_predited_data)):
        nearest_result = [k for k in k_predited_data[a]]
        buf = [int(patchs[i]) for i in nearest_result]
        #k1 = patchs[k1]
        #k2 = patchs[k2]
        #k3 = patchs[k3]
        trans_closest.append(buf)

    trans_closest = np.array(trans_closest)
    #print("[TimeMeasurement] KNN patch search from k-result Time : ", time.time() - knn_match_time)


    '''
    Search Clothes
    '''
    patchToImage = {}
    with open("patch_information.csv") as f:
        patch_inform = csv.reader(f)
        for item in patch_inform:
            try:
                patchToImage[int(item[-1])] = item[0]
            except Exception as e:
                print(e)

    s3_address = "Clothes Storage Endpoint"
    for i in range(0, len(trans_closest)):
        clothes = { j : s3_address + patchToImage[trans_closest[i][j]] for j in range(0, 15)}

    clothes = reduce_v(clothes)
    pairs = {"clothes" : clothes}
    return pairs

def lambda_handler(event, context):
    preprocessing_time = time.time()
    data = event['data']
    data = base64.b64decode(data)
    data = np.frombuffer(data, dtype=np.float64)
    data = np.array([data])
    knn_res, _ = watching.watch(knn_model.kneighbors, [data], name='knn_search_similar_patternIDs')
    distance, k_predited_data = knn_res
    pairs, _ = watching.watch(find_clothe, [k_predited_data], name='knn_collect_clothes_using_patternID')

    return {
        'knnStateCode': 200,
        'body': json.dumps(pairs)
    }
