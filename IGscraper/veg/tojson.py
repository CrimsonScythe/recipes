import json
import pickle

count=0

# for i in range(1,11):
#     if (i==2 or i==1):
#         continue
    

#     with open(f'data{i}', 'rb') as fp:
#         itemList = pickle.load(fp)
        
#         for item in itemList:
            
#             print(item)
#             print(' ')

with open('data7', 'rb') as fp:
    itemList = pickle.load(fp)
    for item in itemList:
        print(item)
        print(' ')

