import random
import string
import re

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download("punkt",quiet="True")
nltk.download("stopwords",quiet="True")

def partB(data):

    # Lowercase the text
    data = data.lower()

    for x in range(len(data)):
        if x=="-":
            data[x]=" "


    # Tokenize the text
    data
    tokens = word_tokenize(data)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]

    # Remove punctuations
    filtered_tokens = [token for token in filtered_tokens if token not in string.punctuation]
    filtered_tokens = [token for token in filtered_tokens if token!="-"] #removing hyphens. strings.punctuations didn't work
    filtered_tokens = [re.sub(r'\b-\b', '', token) for token in filtered_tokens]  #removing hyphens. above didn't work as well 

    # Remove blank space tokens
    filtered_tokens = [token for token in filtered_tokens if len(token) > 0]

    return " ".join(filtered_tokens)

def printrandom(pre):

    after=partB(pre)

    # print(" Before preprocessing \n")
    # print(pre)
    # print()
    # print(" After preprocessing \n")

    # print(after)

def fileupdate():
    for i in range(1, 1401):


        if i<6: #storing five random files before preprocessing

            # print("#"+str(i)+"\n")

            r=random.randint(1,1400)
            tempfile=f"CSE508_Winter2023_Dataset/cranfield{str(r).zfill(4)}"

            with open(tempfile, "r") as file:
                pre = file.read()

            printrandom(pre)


        file_name = f"CSE508_Winter2023_Dataset/cranfield{str(i).zfill(4)}"
        with open(file_name, "r") as file:
            text = file.read()
        final_t = partB(text)
        with open(file_name, "w") as file:
            file.write(final_t)
            
if __name__ == "__main__":
    fileupdate()




