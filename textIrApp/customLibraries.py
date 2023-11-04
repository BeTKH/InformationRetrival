import re
import nltk
import collections
import numpy as np


# nltk tools
stopwords_en = nltk.corpus.stopwords.words("english")
ps = nltk.stem.PorterStemmer()

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


# remove special characters
characters_to_remove = "[\[\]\(\){},.!\?;:\-_'\"]"


def cleanQuery(query):
    query = casefoldQuery(query)
    query = normalizeQuery(query, characters_to_remove)
    query = filterStopWordsQuery(query, stopwords_en)
    query = [ps.stem(word) for word in query]
    return query


# casefold all files
def casefold_allfiles(corpus):
    return [casefoldQuery(file) for file in corpus]

# clean all files


def normalize_allfiles(files):
    return [normalizeQuery(file, characters_to_remove) for file in files]


def remove_stopwords_allfiles(corpus):
    return [filterStopWordsQuery(file, stopwords_en) for file in corpus]

# stems all words in a file


def stem_allfiles(corpus):
    return [stemQuery(file) for file in corpus]


def clean_Entirefiles(corpus):

    # casefold  chars
    corpus = casefold_allfiles(corpus)

    # clean special chars
    corpus = normalize_allfiles(corpus)

    # remove stop words
    corpus = remove_stopwords_allfiles(corpus)

    # stemming
    cleanCorpus = stem_allfiles(corpus)

    return cleanCorpus


# Run corpus summary on each document
def summarize_Entirefiles(corpus):
    counters = [collections.Counter(file) for file in corpus]

    # create empty counter
    counter_tmp = collections.Counter()

    # iterate counter and sum up
    for c in counters:
        counter_tmp += c
    return (counter_tmp, counters)


# load all files from gutenberg corpus
file_names = nltk.corpus.gutenberg.fileids()


def load_allfiles():
    return [nltk.corpus.gutenberg.words(file) for file in file_names]


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


# perform query
def query_documents(tdm, terms, query):
    idxs = [terms.index(word) for word in query if word in terms]
    return tdm[idxs].sum(axis=0)
