# Experiment
import nltk
import Methods as m
from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint
ex = 'Text'

print("--Defining Stop Words---")
stop_words = m.read_stopwords()


print("--text preprocessing---")


def preprocess(item):
    token_text = m.text_cleaning(item, stop_words)
    token_text = nltk.pos_tag(token_text)
    return token_text


sent = preprocess(ex)
print(sent)
pattern = 'NP: {<DT>?<JJ>*<NN>}'
cp = nltk.RegexpParser(pattern)
cs = cp.parse(sent)
iob_tagged = tree2conlltags(cs)
pprint(iob_tagged)


nouns = []
verbs = []
others =[]
for itemm in sent:
    if itemm[1] == 'NN':
        nouns.append(itemm[0])
    elif itemm[1] == 'VB':
        verbs.append(itemm[0])
    elif itemm[1] == 'VBG':
        verbs.append(itemm[0])
    elif itemm[1] == 'VBD':
        verbs.append(itemm[0])
    elif itemm[1] == 'JJ':
        others.append(itemm[0])
    elif itemm[1] == 'NNP':
        nouns.append(itemm[0])


print(nouns)
print(verbs)
print(others)
