### count the number of recipes in each category
import pickle

file_path = '/home/andrew/zhubin/im2recipe-Pytorch/data/classes1M.pkl'
cat_num = {}
categories = []

with open(file_path) as f:
	rec2cat = pickle.load(f)
	catlist = rec2cat.values()
	categories =  pickle.load(f)

for i in range(1048):
	cat_num[i] = 0

for v in catlist:
	cat_num[v] = cat_num[v] + 1

print('done')
pickle.dump(cat_num, open('cat_num.pkl', 'wb')) 


