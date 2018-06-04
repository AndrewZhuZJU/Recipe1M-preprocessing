import os
import numpy as np

file_path = 'rec2imgID.txt'
base_path = '/vireo00/Andrew/recipe1M/test/'


num = 20000
count = 0
imageName = []
with open(file_path) as f:
	while(True):
		if(count >= num):
			break
		line = f.readline()
		img_name = line.split(' ')[1]
		img_name = img_name.strip()
		#imageName.append(img_name)
		img_path = img_name.split('.')[0]
		img_path_final = base_path
		for i in range(4):
			img_path_final = img_path_final + img_path[i] + '/'
		img_path_final = img_path_final + img_name
		print('cp ' + img_path_final + ' V2-20000')
		os.system('cp ' + img_path_final + ' V2-20000')
		count = count + 1
		print(count)

#np.save('imgName20000.npy' , imageName)

