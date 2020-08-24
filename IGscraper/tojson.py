import json
import pickle

count=0

for i in range(1,11):
    if (i==1):
        continue
    
    
    with open(f'data{i}', 'rb') as fp:
        itemList = pickle.load(fp)
        print(i)    
        for item in itemList:
            count+=1
            # print(item)
            # print(' ')

print(count)