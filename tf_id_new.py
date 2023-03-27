import pickle
import numpy as np
import math
from q1b import partB #pre processing


with open('unigram_index.pickle', 'rb') as f:
        unigram_index = pickle.load(f)


vocab = list(unigram_index.keys())
total_docs = 1400
vocab_size = len(vocab)
tf_idf_matrix = np.zeros((total_docs, vocab_size))

def tf_idf_cal(scheme):
        
    #
    df = {}
    for term in vocab:
        df[term] = len(unigram_index[term])

    
    idf = {}
    for term in vocab:
        idf[term] = np.log((total_docs)/(df[term]+1))

    
    docs = []
    for i in range(1, total_docs+1):
        file_name = f"CSE508_Winter2023_Dataset/cranfield{str(i).zfill(4)}"
        with open(file_name, "r") as file:
            data = file.read()
        docs.append(data)

    
    for i, doc in enumerate(docs):
            words = doc.lower().split()
            tf_list=[]
            for t in words:
                tf_list.append(words.count(t))
                tf_max = max(tf_list)
            for j, term in enumerate(vocab):
                if scheme=="binary":
                    if term in words:
                        tf = 1
                    else:
                        tf=0
                    tf_idf_matrix[i, j] = tf * idf[term]
                if scheme=="raw":
                    tf = words.count(term) 
                    tf_idf_matrix[i, j] = tf * idf[term]
                if scheme =="term_freq":
                    tf = words.count(term) / len(words)
                    tf_idf_matrix[i, j] = tf * idf[term]
                if scheme=="log":
                    tf = words.count(term)
                    tf = np.log(1+tf)
                    tf_idf_matrix[i, j] = tf * idf[term]
                if scheme=="double":
                    tf = words.count(term)
                    tf = 0.5+0.5*(tf/tf_max)
                    tf_idf_matrix[i, j] = tf * idf[term]



    return tf_idf_matrix
        
    

def take_input():
    query = input("What are you looking for?: ")
    query = partB(query).lower().split()
    query_vector = np.zeros(vocab_size)
    for term in query:
        if term in vocab:
            j = vocab.index(term)
            query_vector[j] += 1

    scores_binary = np.dot(query_vector, tf_idf_cal("binary").T)
    scores_raw = np.dot(query_vector, tf_idf_cal("raw").T)
    scores_term_freq = np.dot(query_vector, tf_idf_cal("term_freq").T)
    scores_log = np.dot(query_vector, tf_idf_cal("log").T)
    scores_double = np.dot(query_vector, tf_idf_cal("double").T)

    
    top_docs_binary = np.argsort(scores_binary)[::-1][:5]
    top_docs_scores_binary = scores_binary[top_docs_binary]
    print("BINARY SCHEME\n")
    for i, id in enumerate(top_docs_binary):
        print("Document- {}, Score- {}".format(id+1, top_docs_scores_binary[i]))
    
    top_docs_raw = np.argsort(scores_raw)[::-1][:5]
    top_docs_scores_raw = scores_raw[top_docs_raw]
    print("RAW SCHEME\n")
    for i, id in enumerate(top_docs_raw):
        print("Document- {}, Score- {}".format(id+1, top_docs_scores_raw[i]))
    
    top_docs_term_freq = np.argsort(scores_term_freq)[::-1][:5]
    top_docs_scores_term_freq = scores_term_freq[top_docs_term_freq]
    
    print("TERM FREQUENCY SCHEME\n")
    for i, id in enumerate(top_docs_term_freq):
        print("Document- {}, Score- {}".format(id+1, top_docs_scores_term_freq[i]))
    
    top_docs_log = np.argsort(scores_log)[::-1][:5]
    top_docs_scores_log = scores_log[top_docs_log]
    print("LOG NORMALIZATION SCHEME\n")
    
    for i, id in enumerate(top_docs_log):
        print("Document- {}, Score- {}".format(id+1, top_docs_scores_log[i]))
    
    top_docs_double = np.argsort(scores_double)[::-1][:5]
    top_docs_scores_double = scores_binary[top_docs_double]
    print("DOUBLE NORMALIZATION SCHEME\n")
    for i, id in enumerate(top_docs_double):
        print("Document- {}, Score- {}".format(id+1, top_docs_scores_double[i]))
    
    


take_input()
