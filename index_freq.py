'''
inverted index with frequency
auther: Yanyi Liang (642967)
date: 14/4/2015
'''

from pprint import pprint as pp
from glob import glob
from collections import Counter
import nltk
import math
import datetime

begin_time = datetime.datetime.now()

try:
    raw_input
except:
    raw_input = input

def tokenize(raw_text):
    # make the file in lower case
    import string
    import nltk
    a_text = filter(lambda x: x in string.printable, raw_text)
    low_text = a_text.lower()
    #remove punctuation
    tokens = nltk.RegexpTokenizer(r'\w+').tokenize(low_text)
    #stem the tokens
    s_tokens = []
    st = nltk.stem.LancasterStemmer()
    # st = nltk.stem.WordNetLemmatizer()
    for t in tokens:
        s_t = st.stem(t)
        # s_t = st.lemmatize(t)
        s_tokens.append(s_t)
    #remove stopwords
    stop = nltk.corpus.stopwords.words('english')
    flitered_words = [w for w in s_tokens if not w in stop]
    return flitered_words


def bulid_index(fileglob='blogs/*.txt'):
# def bulid_index(fileglob='t210/*.txt'):
    index = {}
    words = set()
    for doc in glob(fileglob):
        with open(doc, 'r') as myfile:
            original_text = myfile.read()
            plain_text = tokenize(original_text)  # text after tokenize
                # words |= set(plain_text)
            for wrd in set(plain_text):
                if wrd in words:
                    index[wrd].append([doc.split('\\')[-1], plain_text.count(wrd)])
                else:
                    words.add(wrd)
                    index[wrd]=[]
                    index[wrd].append([doc.split('\\')[-1], plain_text.count(wrd)])
    return index

inverted_index = bulid_index()
finish_time = datetime.datetime.now()
timedelta = finish_time - begin_time
print timedelta

import cPickle as pickle
indexa = open( "index_freq_b.p", "wb" )
pickle.dump(inverted_index, indexa )
indexa.close()