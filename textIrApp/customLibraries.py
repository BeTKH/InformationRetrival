import re
import nltk
import collections
import numpy as np


ps = nltk.stem.PorterStemmer()


"""
-----------------------------------------------------------------------------------------
DATA LOADING Function(s):

    load_allfiles()
    



DATA CLEANING FUNCTIONS: 


    - cleanQuery() "cleans up" query texts using: 

        casefoldQuery()           
        normalizeQuery()            
        filterStopWordsQuery()      
        stemQuery()                  
        stemQuery()

    - clean_Entirefiles() "cleans up" entire files (corpus) using:

        casefold_allfiles()
        normalize_allfiles()
        remove_stopwords_allfiles()
        stem_allfiles()

        

Term Document Matrx building: 

    summarize_Entirefiles()
    create_term_document_matrix()


QUERY PROCESSING:  

    query_documents()



Query Optimization:


-----------------------------------------------------------------------------------------
"""


"""
-----------------------------------------------------------------------------------------
DATA LOADING 
-----------------------------------------------------------------------------------------
"""


def load_allfiles():

    # load all files from gutenberg corpus
    file_names = nltk.corpus.gutenberg.fileids()

    return [nltk.corpus.gutenberg.words(file) for file in file_names]


"""
-----------------------------------------------------------------------------------------
CLEAN UP QUERY TEXT  
-----------------------------------------------------------------------------------------
"""
# case folding


def casefoldQuery(file):
    return [word.casefold() for word in file]


# cleaning special characters
def normalizeQuery(file, removelist):
    return [token for token in [re.sub(removelist, '', word) for word in file]
            if token != '']


# select words that are not in the stopword list
def filterStopWordsQuery(file, wordlist):
    result = []
    for word in file:
        if not word in wordlist:
            result.append(word)
    return result


# stems all words in a file
def stemQuery(file):
    return [ps.stem(token) for token in file]


def cleanQuery(query):

    query = casefoldQuery(query)

    # remove special characters
    characters_to_remove = "[\[\]\(\){},.!\?;:\-_'\"]"
    query = normalizeQuery(query, characters_to_remove)

    # nltk tools
    stopwords_en = nltk.corpus.stopwords.words("english")
    query = filterStopWordsQuery(query, stopwords_en)

    query = [ps.stem(word) for word in query]
    return query


"""
-----------------------------------------------------------------------------------------
CLEAN UP ALL FILES ( entire corpus)
-----------------------------------------------------------------------------------------
"""
# casefold all files


def casefold_allfiles(corpus):
    return [casefoldQuery(file) for file in corpus]


# clean special characters
def normalize_allfiles(files):

    # remove special characters
    characters_to_remove = "[\[\]\(\){},.!\?;:\-_'\"]"
    return [normalizeQuery(file, characters_to_remove) for file in files]


def remove_stopwords_allfiles(corpus):
    stopwords_en = nltk.corpus.stopwords.words("english")
    return [filterStopWordsQuery(file, stopwords_en) for file in corpus]

# stems all words in a file


def stem_allfiles(corpus):
    return [stemQuery(file) for file in corpus]


def clean_Entirefiles(corpus):

    corpus = casefold_allfiles(corpus)
    corpus = normalize_allfiles(corpus)
    corpus = remove_stopwords_allfiles(corpus)
    cleanCorpus = stem_allfiles(corpus)

    return cleanCorpus


"""
-----------------------------------------------------------------------------------------

BUILD TERM-DOCUMENT-MATRIX
   
-----------------------------------------------------------------------------------------
"""


# Run corpus summary on each document
def summarize_Entirefiles(corpus):
    counters = [collections.Counter(file) for file in corpus]

    # create empty counter
    counter_tmp = collections.Counter()

    # iterate counter and sum up
    for c in counters:
        counter_tmp += c
    return (counter_tmp, counters)


def create_term_document_matrix(corpus):
    """ 
    takes: collection of clean documents ( corpus) 
    retuns: term-document matrix and all terms 

    """

    # get the summary of the corpus
    counter_corpus, counter_documents = summarize_Entirefiles(corpus)

    # create an empty matrix with the correct dimension
    tdm = np.zeros((len(counter_corpus), len(corpus)))

    for idx, word in enumerate(counter_corpus):
        for document_id in range(len(corpus)):
            if word in counter_documents[document_id]:
                tdm[idx, document_id] = counter_documents[document_id][word]
    return (tdm, list(counter_corpus.keys()))


"""
-----------------------------------------------------------------------------------------

QUERY EXCUTION

query_documents()

    retruns documents' relevance score array sth like 

    result = array([8.670e+02, 3.000e+00, 2.000e+00, 2.979e+03, 3.000e+00, 0.000e+00,
       0.000e+00, 0.000e+00, 3.000e+00, 6.000e+00, 2.000e+00, 1.000e+00,
       8.000e+00, 6.000e+00, 3.890e+02, 3.000e+00, 1.000e+00, 0.000e+00])
    
-----------------------------------------------------------------------------------------
"""


def query_documents(tdm, terms, query):
    idxs = [terms.index(word) for word in query if word in terms]
    documentScore = tdm[idxs].sum(axis=0)
    return documentScore


"""
-----------------------------------------------------------------------------------------
PRESENT DATA by order of relevance  
-----------------------------------------------------------------------------------------
"""
# map files names with relevance score in a dict


def orderByRelevance(docScore):

    file_names = [title.split('.')[0]
                  for title in nltk.corpus.gutenberg.fileids()]

    # normalize scores
    docScore = (docScore / np.sum(docScore)) * 100

    # round it
    docScore = np.round(docScore, 1)

    # map score with file names
    file_score_map = {file_names[i]: docScore[i]
                      for i in range(len(file_names))}

    # Filter values greater than 0
    file_score_filtered = {key: value for key,
                           value in file_score_map.items() if value > 0}

    # Sort in descending order
    file_score_sorted = sorted(
        file_score_filtered.items(), key=lambda x: x[1], reverse=True)

    return file_score_sorted


"""
-----------------------------------------------------------------------------------------
QUERY OPTIMIZATION 

logScale_tf()
scale_tfidf

-----------------------------------------------------------------------------------------
"""


def logScale_tf(tdm):
    return np.log1p(tdm)


def scale_tfidf(tdm_):
    tdm_ = logScale_tf(tdm_)
    tmp = tdm_ != 0
    num_documents = tdm_.shape[1]

    idf = np.log(num_documents/tdm_.sum(axis=1))
    return (tdm_.T * idf).T
