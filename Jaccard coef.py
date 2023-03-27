
import pickle
import numpy as np
import math
from q1b import partB #pre processing


# Create sets of terms
# for query and documents
query=input("What are you looking for?: ")
query=partB(query)
query_terms=set(list(map(str,query.split(" "))))
print(query_terms)

docs_dict = {}
for i in range(1, 1401):
    file_name = f"CSE508_Winter2023_Dataset/cranfield{str(i).zfill(4)}"
    with open(file_name, "r") as file:
        data = file.read()
        data = set(list(map(str,data.split(" "))))
    docs_dict[i]=data

jaccard_coeff_values = []
for i in range(1,1401):
    intersection_set= query_terms.intersection(docs_dict[i])
    intersection = len(intersection_set)
    union_set = query_terms.union(docs_dict[i])
    union = len(union_set)
    if union == 0:
        jaccard=0
    else:
        jaccard = intersection / union
    jaccard_coeff_values.append((i, jaccard))

# Rank documents based on Jaccard coefficient value
documents_descending_order = sorted(jaccard_coeff_values, reverse=True)
top_10 = documents_descending_order[0:10]


# Print top 10 documents
for i, jaccard in top_10:
    print("Document {}: Jaccard coefficient = {:.4f}".format(i+1, jaccard))
    print()
