# count the recipe and image in each category

import pickle
import json
import os

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


'''
#layer2_recIDs = pickle.load(open('layer2_recIDs.pkl', 'r'))
#print(len(layer2_recIDs))
num_imgs = {}

for i in range(1048):
	num_imgs[i] = 0

with open(class1M_path) as f:
	classes = pickle.load(f)
	categories = pickle.load(f)
	count = 0
	for item in classes:
		count = count + 1
		print(str(count) + '  processing ' + item)
		if(not classes[item]):
			continue
		if(item in layer2_recIDs):
			num_imgs[classes[item]] = num_imgs[classes[item]] + 1

#pickle.dump(num_imgs, open('num_imgs_v3.pkl', 'wb'))

'''

'''
# get recipes
sel_cat = [4,3,1043,1009,15,53,1019,27]
#structure:<dict:<category, [recipeID, imgID]>>
sel_cat_rec = {}
for item in sel_cat:
	sel_cat_rec[item] = []

#print sel_rec_img

with open(class1M_path) as f:
	classes = pickle.load(f)
	categories = pickle.load(f)
	count = 0
	for item in classes:
		count = count + 1
		#if(count > 1000):
		#	break
		print(str(count) + '  processing ' + item)
		if(not classes[item]):
			continue
		if(classes[item] in sel_cat):
			sel_cat_rec[classes[item]].append(item)

#print(sel_cat_rec)
pickle.dump(sel_cat_rec, open('sel_cat_rec.pkl', 'wb'))

'''

##get imgs
sel_cat = [4,3,1043,1009,15,53,1019,27]
base_path = '/vireo00/Andrew/recipe1M/'
layer2_recIDs = pickle.load(open('layer2_recIDs.pkl', 'r'))
sel_cat_rec = pickle.load(open('sel_cat_rec.pkl', 'r'))
with open(layer2_path) as f:
	layer2 = json.load(f)
	for cat in sel_cat:
		cat_path = './dataset/' + str(cat)
		if(not os.path.exists(cat_path)):
			os.mkdir(cat_path)
		out = open(cat_path + '/rec_img.txt', 'w')
		for rec in sel_cat_rec[cat]:
			if(not rec in layer2_recIDs):
				continue
			img_id = layer2[layer2_recIDs.index(rec)]['images'][0]['id']
			print(img_id)
			out.write(rec + '   ' + img_id +'\n')
			img_path = img_id.split('.')[0]
			img_path_final = ''
			for i in range(4):
			  img_path_final = img_path_final + img_path[i] + '/'
			img_path_final = img_path_final + img_id
			if(os.path.exists(base_path + 'train/' + img_path_final)):
				img_path_final = base_path + 'train/' + img_path_final
			elif(os.path.exists(base_path + 'test/' + img_path_final)):
				img_path_final = base_path + 'test/' + img_path_final
			else:
				img_path_final = base_path + 'val/' + img_path_final
			print('cp ' + img_path_final + ' ' + cat_path)
			os.system('cp ' + img_path_final + ' ' + cat_path)








