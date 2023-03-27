import pickle
from collections import defaultdict

index = defaultdict(list) #unigram index

for doc_id in range(1,1401):

    file_name = f"CSE508_Winter2023_Dataset/cranfield{str(doc_id).zfill(4)}"
    with open(file_name, "r") as file:
        text = file.read()

    tokens = text.split()
    unique=[] #unique is updated/reset for every iteration i.e for every file

    for token in tokens:
        if token not in unique: #only if token is not in unique we will add it in index
            index[token].append(doc_id)
            unique.append(token) 
            #this is so we don't store same doc ids multiple time for the same index


with open("unigram_index.pickle", "wb") as file:
    pickle.dump(index, file)

with open("unigram_index.pickle", "rb") as file:
    index = pickle.load(file)
