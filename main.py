import Methods as m
import Stanford
import  nltk
from nltk.tokenize import word_tokenize
import get_Old_Tweets_re as got
stop_words = m.read_stopwords()

ordering = []
keystring = []
s = ''
user_text ='' # Input tweet here
print("news", user_text)
tokenized_text = word_tokenize(user_text)
news_text = str(m.text_cleaning(user_text, stop_words))

#----getting keywords ----
candidate_keywords = Stanford.extract_candidate_keywords(news_text)
candidate_keywords = [m.lower() for m in candidate_keywords]
keywords = list(dict.fromkeys(candidate_keywords))#remove duplicates
print("keywords", keywords)
#----getting keywords---

#---Ordering the keywords---
for word in tokenized_text:
    for kword in keywords:
        if word.lower() == kword:
            ordering.append(kword)
            keywords.remove(kword)

ordering = ordering + keywords
for x in range(len(ordering)):
    s = s + ordering[x] + " "
    if len(s.split()) == 3:
        keystring.append(s)
        s = ''
    elif x == len(ordering)-1:
        keystring.append(s)
print("keystring", keystring)
#---Ordering the keywords---

# --- Calling Get)oldTweets---
got.getTweets(keystring)
# --- Calling Get)oldTweets---