# count the recipe and image in each category

import pickle
import json

layer2_path = '/home/andrew/zhubin/im2recipe-Pytorch/data/recipe1M_layers/layer2.json'
class1M_path = '/home/andrew/zhubin/im2recipe-Pytorch/data/classes1M.pkl'

'''
# get all the recipe ID of layer2
layer2_recIDs = []

with open(layer2_path) as f:
	layer2 = json.load(f)
	for i in range(len(layer2)):
		layer2_recIDs.append(layer2[i]['id'])

pickle.dump(layer2_recIDs, open('layer2_recIDs.pkl', 'wb'))
'''

layer2_recIDs = pickle.load(open('layer2_recIDs.pkl', 'r'))
print(len(layer2_recIDs))
num_imgs = {}

for i in range(1048):
	num_imgs[i] = 0

with open(class1M_path) as f:
	classes = pickle.load(f)
	categories = pickle.load(f)
	for item in classes:
		if(item in layer2_recIDs):
			num_imgs[classes[item]] = num_imgs[classes[item]] + 1

pickle.dump(num_imgs, open('num_imgs.pkl', 'wb'))








