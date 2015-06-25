'''
calculate cos similarity between query and documents
return top N relavant documents
auther: Yanyi Liang (642967)
date:14/4/2015
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

# file_folder = raw_input('enter a dictionary:')
import cPickle as pickle
inverted_index = pickle.load(open("index_freq_b.p", "rb")) 

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

def idf(t,index=inverted_index):
    import os
    files = os.listdir('blogs/')
    # print files
    total_file_num = len(files)
    # print total_file_num
    idf_t = math.log(float(total_file_num)/len(index[t]))
    # print len(index[t])
    return idf_t

def tf(t,d,index=inverted_index):
    f = 0
    if index.has_key(t):
        for item in index[t]:
            if item[0]==d:
                f = item[1]
                break
    tf_dt = math.log(1 + float(f))
    # tf_dt = f
    return tf_dt

def cos_dist(q,d):
    a_d = 0
    for t in q:
        a_d = a_d + tf(t,d,) * idf(t,)
        # print a_d
    return a_d

def doc_rank(q,docs):
    doc_score = {}
    for d in docs:
        cos_score = cos_dist(q,d)
        doc_score[d] = cos_score
    sorted_doc_score = sorted(doc_score, key=doc_score.__getitem__, reverse=True)
    formmated_result = []
    for item in sorted_doc_score[:100]:
        formmated_result.append(item[6:-4])
    # print formmated_result
    return formmated_result

query = '"March of the Penguins"'
plain_query = tokenize(query)
result = doc_rank(plain_query,glob('blogs/*.txt'))
print result

finish_time = datetime.datetime.now()
timedelta = finish_time - begin_time
print timedelta


