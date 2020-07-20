import json
import pickle

with open('personal1.json') as f:
    data = json.load(f)
    l = []
    for i in data:
        tags = data[i]
        if '#' in tags:
            l.append(tags)

with open('tags.txt', "wb") as fp:
    pickle.dump(l, fp)

# with open("tags.txt", "rb") as ftp:
#     b = pickle.load(ftp)
#     print(b)