import csv
from math import log2

burner_list = {} #will store the data after splitting/parsing according to requirements

with open('IR-assignment-2-data (2).txt') as f:
    temp = csv.reader(f, delimiter=' ')
    for entry in temp:
        if int(entry[0]) == 4:
            split_product = entry[1].split()   #temp holder after splitting URLs and relevance score
            for grouping in split_product:  #for each of the pairings in the pid
                URL_num, separator, relevance_score = grouping.partition(':')   #part before : goes to URL_num, after to relevance_score
                if URL_num in burner_list:  #checking in with the burner list if entry of URL has already been made
                    burner_list[URL_num].append((entry[0], int(relevance_score)))
                else:
                    burner_list[URL_num] = [(entry[0], int(relevance_score))] #adding to the burner list if not a
disc_values = {}  #storing DCG values acc to formula

def calc_DCG(scores):   #DCG calculation function
    DCG = 0.0
    sc_len = len(scores)
    for i, score in enumerate(scores):
        DCG +=((score)/ log2(i + 2)   #class slides formula given
    return DCG

for URL_num in burner_list:
    relevance_scores = []
    for element in burner_list[URL_num]:
        relevance_scores.append(element[1])
    disc_values[URL_num] = calc_DCG(relevance_scores)

sort_by_max = sorted(burner_list, key=lambda x: disc_values.get(x, 0), reverse=True)

