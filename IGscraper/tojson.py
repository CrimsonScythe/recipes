import json
import pickle

with open('data', 'rb') as fp:
    itemList = pickle.load(fp)

# print(itemList)
for item in itemList:
    print('\n')
    print(item)    