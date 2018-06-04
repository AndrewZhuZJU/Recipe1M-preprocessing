##################################################
# combine the fake image and groung truth together
##################################################

from PIL import Image
import numpy as np

fake_path = '/home/andrew/zhubin/StackGAN-Pytorch/output/coco_stageII_2018_05_30_10_21_13/Model/'
num_img = 100
count = 0

rec_id = []
real_img = []

with open('rec2imgID.txt') as f:
	while(True):
		line = f.readline()
		line = line.strip().split(' ')
		rec_id.append(line[0])
		real_img.append(line[1])
		count = count + 1
		if(count >= num_img):
			break

print(rec_id)
print(real_img)

with open('recipes.npy') as f:
	rec = np.load(f)
	rec_item = rec.item()
	count = 0
	for rid in rec_id:
		print(count)
		title = rec_item[rid]['title']
		title = title.replace('/', '')
		r_img = Image.open('V2-20000/' + real_img[count])
		f_img = Image.open(fake_path + 'netG_epoch_90/' + str(count) + '.png')
		res_img = Image.new('RGB', (256*2, 256))
		r_img = r_img.resize((256,256))
		res_img.paste(r_img, (0,0))
		res_img.paste(f_img, (256,0))
		print('saving ' + title)
		res_img.save(fake_path + 'netG_epoch_90_result/' + str(count) + '_' + title + '.jpg')
		count = count + 1






