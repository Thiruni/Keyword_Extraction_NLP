# Experiment
import nltk
from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()
#sp = spacy.load('en_core_web_sm')

doc = nlp('European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices')
# print(doc)
pprint([(X.text, X.label_) for X in doc.ents])