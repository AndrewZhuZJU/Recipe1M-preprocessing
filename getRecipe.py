#####################################
# author: Andrew
# get the recipe of chosen recipe IDs 
#####################################

import json
import numpy as np


l1_path = '/home/andrew/zhubin/im2recipe-Pytorch/data/recipe1M_layers/layer1.json'
recipes = {}
recIDs = []

with open('rec2imgID.txt') as f:
	while(True):
		recID = f.readline()
		if(not recID):
			break
		recID = recID.split(' ')[0]
		recIDs.append(recID)

print(len(recIDs))

with open(l1_path) as f:
	layer1 = json.load(f)
	for item in layer1:
		print('processing ' + item['id'])
		if(item['id'] in recIDs):
			recipes[item['id']] = item

np.save('recipes.npy', recipes)

'''
tips:
if a variable <type 'dict'> saves as npy, when load as V, one should use V.item()
to get the dict value of the variable. 
'''

