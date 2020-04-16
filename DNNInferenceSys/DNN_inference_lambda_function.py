import time
module_start = time.time()
import pickle
import numpy as np
from PIL import Image
from PIL import ImageFile
import json
from io import BytesIO
import base64
import torch
from dl_model import Net
import urllib3
module_end = time.time()
print("[TimeMeasurement] module loaded time : ", module_end - module_start)

from watcher import Watcher
watching = Watcher(td=True)

model, _ = watching.watch(pickle.load, [open('torch_model.pkl','rb')], name='torch_loaded')
model = model.double()
print("[BreakTime] Torch no need model read time")

from watcher import Watcher
watching = Watcher(td=True)
http = urllib3.PoolManager()

ImageFile.LOAD_TRUNCATED_IMAGES = True
def image_decoder(baseImg):
    x = base64.b64decode(baseImg) # base64 to bytes
    splited_x = x.split(b'\r\n') # split bytes
    data_decoded_bytes = splited_x[4]
    print(splited_x)
    try:
        data_decoded_bytes.decode('utf-8')
        data_decoded_bytes = base64.b64decode(data_decoded_bytes)
        print(data_decoded_bytes)
    except:
        print("need not decode base64.")
        print(data_decoded_bytes)
    return data_decoded_bytes

def normalize_minmax(input_x):
    input_x = np.abs((input_x - np.min(input_x)) / (np.min(input_x) - np.max(input_x)))
    return input_x

def inference(tensor):
    x = torch.tensor([tensor])
    return model(x)

def req_knn(feature):
    url = 'Endpoint KNN Mining System'

    headers = {'Content-Type': 'image/jpeg'}
    res = http.request("PUT", url, body=feature.tobytes(), headers=headers)
    return res

def lambda_handler(event, context):

    img = event['body-json']
    img_shape = event['params']['querystring'] # is no need...

    img = image_decoder(img) # extract bytes image from a encoded base64.
    img = Image.open(BytesIO(img))
    img = img.resize((64, 64))
    img = np.array(img, np.float64)
    img = normalize_minmax(img)
    img = np.transpose(img, (2,0,1))
    img = np.array([img[2],img[1],img[0]]) # RGB -> BGR. That is Torch specified.

    x = torch.tensor([img])
    model_out, _ = watching.watch(model, [x], name='find_feature_vector')
    _, feature = model_out

    feature = feature.detach().cpu().numpy()
    res, _ = watching.watch(req_knn, [feature], name="find_similar_clothes")

    res = res.data.decode('utf-8')
    return res
