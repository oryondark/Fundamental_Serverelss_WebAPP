import os, sys

import shutil
def remove_cache(path):
    shutil.rmtree(path)
    print(path)
def greedy_search(path):
	#path = os.path.join(root, item)
	res = check_dir(path)
	#print(path) # Debug
	if (path.split('/')[-1].find("__pycache__") >= 0):
		remove_cache(path)
	else:
		if res == True:
			for i in os.listdir(path):
				sub_path = os.path.join(path, i)
				greedy_search(sub_path)
		else:
			count = 0
			#print(path)
			#uploader_s3(path)
def check_dir(path):
	if os.path.isdir(path) == True:
		return True
	else:
		return False

root_path = '.'
for i in os.listdir(root_path):
	if i.find('DS_Store') > 0:
		print("Pass DS store file")
		pass
	else:
		sub_path = os.path.join(root_path, i)
		print("search for sub_path")
		greedy_search(sub_path)
