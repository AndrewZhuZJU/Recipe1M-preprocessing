# select categories to form the new dataset
# get images from selected categories
import pickle
import os

'''
num = 50 # top num categories
out = open('sel_cat.txt', 'w')
with open('cat_num.pkl') as f:
	cat_num = pickle.load(f)

	with open('../data/classes1M.pkl') as ff:
		classes = pickle.load(ff)
		cat_name = pickle.load(ff)
		cat_num = sorted(cat_num.items(), key = lambda d:d[1], reverse = True)
		#print(cat_num)
		#print(type(cat_num))
		for i in range(num):
			print('%-10d %-20s %-10d' %(cat_num[i][0], cat_name[cat_num[i][0]], cat_num[i][1]))
			#out.write(str(cat_num[i][0]) + '   ' + cat_name[cat_num[i][0]] + '  ' + str(cat_num[i][1]) + '\n')
			out.write('%-10d %-20s %-10d \n' %(cat_num[i][0], cat_name[cat_num[i][0]], cat_num[i][1]))

	out.close()
'''

def getImages():
	sel_cat = [4,3,1043,1009,15,53,1019,27]

