import pickle
import numpy as np
import math
from q1b import partB #pre processing

# Load the unigram index matrix from the pickle file
with open('unigram_index.pickle', 'rb') as f:
    unigram_matrix = pickle.load(f)

# Create a vocabulary list containing all the terms in the matrix
vocab = list(unigram_matrix.keys())
total_docs = 1400
vocab_size = len(vocab)
tf_idf_matrix = np.zeros((total_docs, vocab_size))

# Compute the document frequency (df) value for each term in the vocabulary
df = {}
for term in vocab:
    df[term] = len(unigram_matrix[term])

# Compute the IDF value for each term in the vocabulary
idf = {}
for term in vocab:
    idf[term] = np.log((total_docs)/(df[term]+1))

# Load the documents
docs = []
for i in range(1, total_docs+1):
    file_name = f"CSE508_Winter2023_Dataset/cranfield{str(i).zfill(4)}"
    with open(file_name, "r") as file:
        data = file.read()
    docs.append(data)

# Calculate the TF-IDF matrix
for i, doc in enumerate(docs):
    words = doc.lower().split()
    for j, term in enumerate(vocab):
        tf = words.count(term) / len(words)
        tf_idf_matrix[i, j] = tf * idf[term]

def take_input():
    query = input("What are you looking for?: ")
    query = partB(query).lower().split()
    query_vector = np.zeros(vocab_size)
    for term in query:
        if term in vocab:
            j = vocab.index(term)
            query_vector[j] += 1

    # Compute TF-IDF score for query
    scores = np.dot(query_vector, tf_idf_matrix.T)

    # Get top 5 relevant documents
    top_docs_idx = np.argsort(-scores)[:5]
    top_docs_scores = scores[top_docs_idx]

    # Print top 5 relevant documents and their scores
    for i, idx in enumerate(top_docs_idx):
        print(f"Rank {i+1} - Document index: {idx+1}, Score: {top_docs_scores[i]}")

take_input()
