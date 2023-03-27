
import pickle
import numpy as np
import math
from q1b import partB #pre processing


# Create sets of tokens for query and documents
query=input("What are you looking for?: ")
query=partB(query)
query_tokens=set(list(map(str,query.split(" "))))
with open('unigram_index.pickle', 'rb') as f:
    unigram_matrix = pickle.load(f)
document_tokens = [set(unigram_matrix.keys())]

# Calculate Jaccard coefficient for each document
jaccard_values = []
for i in range(1400):
    intersection = len(query_tokens.intersection(document_tokens[i]))
    union = len(query_tokens.union(document_tokens[i]))
    jaccard = intersection / union
    jaccard_values.append((i, jaccard))

# Rank documents based on Jaccard coefficient value
top_10_documents = sorted(jaccard_values, key=lambda x: x[1], reverse=True)[0:10]

# Print top 10 documents
for i, jaccard in top_10_documents:
    print(f"Document {i+1}: Jaccard coefficient = {jaccard:.4f}")
    # print(documents[i])
    print()
