import json
import pickle
import numpy as np

layer1_path = '/home/andrew/zhubin/im2recipe-Pytorch/data/recipe1M_layers/layer1.json'
layer2_path = '/home/andrew/zhubin/im2recipe-Pytorch/data/recipe1M_layers/layer2.json'
rec_ids_path = 'rec_ids.pkl'
image_path = '/vireo00/Andrew/recipe1M/test/'

rec_img_ID_path = 'rec2imgID.txt'

def find_image():
	out = open(rec_img_ID_path, 'w')
	file = open(layer2_path)
	layer2 = json.load(file)
	file = open(rec_ids_path)
	rec_ids = pickle.load(file)
	count = 0
	for data in layer2:
		#print(data)
		#break
		count = count + 1
		print('processing %d / %d' %(count, len(layer2)))
		if(data['id'] in rec_ids):
			print("writing " + data['id'])
			out.write(data['id'] + ' ' + data['images'][0]['id'] + '\n')

	out.close()

def get_recipe_embeds():
	
	rec_embeds_path = 'rec_embeds.pkl'
	rec_embeds = pickle.load(open(rec_embeds_path))
	rec_ids = pickle.load(open(rec_ids_path))
	final_rec_embeds = []
	with open(rec_img_ID_path, 'r') as f:
	    while(True):
		    line = f.readline()
		    if(not line):
			   break
		    rec_id = line.split(' ')[0]
		    print(rec_id)
		    final_rec_embeds.append(rec_embeds[np.where(rec_ids==rec_id)])
		    #print(final_rec_embeds)
		    #break;
	np.save('final_rec_embeds.npy', final_rec_embeds)

get_recipe_embeds()




#find_image()
