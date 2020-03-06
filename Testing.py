import Methods as m
import Stanford
import pandas as pd
import re
# import main

# stop_words = m.read_stopwords()


# test_set = pd.read_csv('venv/Data/TestSet3 v7.csv', names=['ID', 'text', 'keywords', 'Person', 'Location', 'Date', 'Organization', 'Nouns', 'Verbs', 'Synonyms'], header=1)
# print(len(test_set))
# print(type(test_set))
# keyword =[]
# text = []
# for record in test_set['keywords']:
#     record = str(record)
#     record = re.sub(r"\n", "", record)
#     l = record.split(",")
#     keyword.append(l)
#
# for txt in test_set['text']:
#     txt = str(txt)
#     text.append(txt)
#
#
# for x in range(len(text)):
#     print(text[x], keyword[x])

from csv import reader
row = []

# read csv file as a list of lists
with open('venv/Data/new_td.csv', 'r', encoding="utf8") as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)
    # print(type(list_of_rows))

    for line in list_of_rows:
        text = str(line[1])
        keywords = str(line[2])
        # print(keywords)

        candidate_keywords = Stanford.extract_candidate_keywords(text)
        candidate_keywords = [m.lower() for m in candidate_keywords]
        new_keywords = list(dict.fromkeys(candidate_keywords))  # remove duplicates
        print(new_keywords)
        print(text + ' | ' + str(new_keywords))
        keycount = len(keywords.split(","))
        x = text + ',' + str(keycount) + ',' + str(len(new_keywords))
        row.append(x)
        print(x)
        print(len(row))
        if(len(row) == 100 ):
            f = open("new_td.txt", "w+", encoding="utf-8")
            f.write("text, keycount, newkeycount\n")
            for i in range(len(row)):
                record = str(row[i])
                f.write("%s\n" % record)
            f.close()


