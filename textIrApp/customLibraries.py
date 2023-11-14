import re
import nltk
import collections
import numpy as np


"""
-----------------------------------------------------------------------------------------
FUNCTIONS USE

DATA LOADING: 
    - load_allfiles()
    
DATA CLEANING: 
    - clean_Text() "cleans up" query texts using: 
    - clean_Files() "cleans up" entire files (corpus) using:

TDM BUILDING:
    - summarize_Entirefiles()
    - create_term_document_matrix()

QUERY PROCESSING:  
    - query_documents()
-----------------------------------------------------------------------------------------
"""


def load_allfiles():

    # load all files from gutenberg
    file_names = nltk.corpus.gutenberg.fileids()

    return [nltk.corpus.gutenberg.words(file) for file in file_names]


"""
-----------------------------------------------------------------------------------------
CLEAN UP QUERY TEXT  
-----------------------------------------------------------------------------------------
"""


# clean text
def clean_Text(tokenList_):

    tokenList_ = casefold_Text(tokenList_)
    tokenList_ = normalize_Text(tokenList_)
    tokenList_ = filterStopWords_Text(tokenList_)
    tokenList_ = stem_Text(tokenList_)
    return tokenList_

# case folding


def casefold_Text(tokenList_):
    return [word.casefold() for word in tokenList_]


# cleaning special characters
def normalize_Text(tokenList_):
    pattern = r"[^a-zA-Z0-9]"
    clean_tokens = [re.sub(pattern, '', token) for token in tokenList_]
    clean_tokens = list(filter(None, clean_tokens))
    return clean_tokens


# select words that are not in the stopword list
def filterStopWords_Text(tokenList_):

    wordlist = nltk.corpus.stopwords.words("english")

    result = []
    for word in tokenList_:
        if not word in wordlist:
            result.append(word)
    return result


# stems all words in a file
def stem_Text(tokenList_):
    ps = nltk.stem.PorterStemmer()
    return [ps.stem(token) for token in tokenList_]


"""
-----------------------------------------------------------------------------------------
CLEAN UP ALL FILES 
-----------------------------------------------------------------------------------------
"""


# clean all files in one go
def clean_Files(files_):

    files_ = casefold_Files(files_)
    files_ = normalize_Files(files_)
    files_ = remove_stopwords_Files(files_)
    cleanCorpus = stem_Files(files_)

    return cleanCorpus


# casefold all files
def casefold_Files(files_):
    return [casefold_Text(file) for file in files_]


# remove special characters
def normalize_Files(files_):
    return [normalize_Text(file) for file in files_]

# remove stop words


def remove_stopwords_Files(files_):
    return [filterStopWords_Text(file) for file in files_]


# stems all words in a file
def stem_Files(files_):
    return [stem_Text(file) for file in files_]


"""
-----------------------------------------------------------------------------------------

BUILD TERM-DOCUMENT-MATRIX
   
-----------------------------------------------------------------------------------------
"""


def create_term_document_matrix(all_files_):
    """ 
    takes: collection of clean documents ( corpus) 
    retuns: term-document matrix and all terms 

    """

    # get the summary of the corpus
    counter_corpus, counter_documents = summarize_Files(all_files_)

    # create an empty matrix with the correct dimension
    tdm = np.zeros((len(counter_corpus), len(all_files_)))

    for idx, word in enumerate(counter_corpus):
        for document_id in range(len(all_files_)):
            if word in counter_documents[document_id]:
                tdm[idx, document_id] = counter_documents[document_id][word]
    return (tdm, list(counter_corpus.keys()))


# count all unique tokens in all files
def summarize_Files(files_):
    counters = [collections.Counter(file) for file in files_]

    # create empty counter
    counter_tmp = collections.Counter()

    # iterate counter and sum up
    for c in counters:
        counter_tmp += c
    return (counter_tmp, counters)


"""
-----------------------------------------------------------------------------------------

QUERY processing

- first clean query text
- then pass it into 

    retruns documents' relevance score array sth like 

    result = array([8.670e+02, 3.000e+00, 2.000e+00, 2.979e+03, 3.000e+00, 0.000e+00,
       0.000e+00, 0.000e+00, 3.000e+00, 6.000e+00, 2.000e+00, 1.000e+00,
       8.000e+00, 6.000e+00, 3.890e+02, 3.000e+00, 1.000e+00, 0.000e+00])
    
-----------------------------------------------------------------------------------------
"""


def query_documents(tdm, terms, queryText_, idf_):

    #  if idf_ is True, apply idf scaling
    if idf_:
        tdm = scale_tfidf(tdm)

    # change query text into tokens
    queryText_ = queryText_.split()

    # clean the tokens
    queryText_clean = clean_Text(queryText_)

    # build score
    idxs = [terms.index(word) for word in queryText_clean if word in terms]
    documentScore = tdm[idxs].sum(axis=0)
    return documentScore


"""
-----------------------------------------------------------------------------------------
PRESENT DATA by order of relevance  
-----------------------------------------------------------------------------------------
"""
# map files names with relevance score in a dict


def mapFilesToScore(docScore):
    file_names = [title.split('.')[0]
                  for title in nltk.corpus.gutenberg.fileids()]
    fileName_score_ = {}
    for file, score in zip(file_names, docScore):
        fileName_score_[file] = score
    return fileName_score_


def orderByRelevance(docScore):

    # normalize scores
    docScore = (docScore / np.sum(docScore)) * 100

    # round it
    docScore = list(np.round(docScore, 1))

    # map file names to score
    fileName_score_map = mapFilesToScore(docScore)

    # sort results in descending order
    fileName_score_Sorted = dict(
        sorted(fileName_score_map.items(), key=lambda item: item[1], reverse=True))

    # Filter values greater than 0
    fileName_score_Sorted = {key: value for key,
                             value in fileName_score_Sorted.items() if value > 0}

    return fileName_score_Sorted


"""
-----------------------------------------------------------------------------------------
PLOT THE RESULT

-----------------------------------------------------------------------------------------
"""


# plot function
def barPlot(dict_, color_='green', title_='Query result of relevant documents'):

    import matplotlib.pyplot as plt
    plt.style.use('bmh')

    labels = list(dict_.keys())
    values = list(dict_.values())

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.bar(labels, values, color=color_)

    ax.xlabel('file names')
    ax.ylabel('Percentage of document\'s relevance')
    ax.title(title_)
    ax.xticks(rotation=90)  # Rotate x-axis labels for better visibility

    return fig


# Convert the Matplotlib plot to a PNG image

def renderPlot(dict_, color_='green', title_='Query result of relevant documents'):

    plot_ = barPlot(dict_, color_='green',
                    title_='Query result of relevant documents')

    from io import BytesIO
    import base64
    from matplotlib.backends.backend_agg import FigureCanvasAgg
    import matplotlib.pyplot as plt
    from django.utils.http import urlsafe_base64_encode

    # Convert the Matplotlib plot to a PNG image
    buffer = BytesIO()
    canvas = FigureCanvasAgg(plot_)
    canvas.print_png(buffer)
    plt.close(plot_)

    # Get the image data as a base64-encoded string
    image_data_base64 = urlsafe_base64_encode(
        buffer.getvalue()).decode('utf-8')

    return image_data_base64


"""
-----------------------------------------------------------------------------------------
QUERY OPTIMIZATION 

logScale_tf()
scale_tfidf

-----------------------------------------------------------------------------------------
"""


def logScale_tf(tdm):
    return np.log1p(tdm+1)


def scale_tfidf(tdm_):
    tdm_ = logScale_tf(tdm_)
    tmp = tdm_ != 0
    num_documents = tdm_.shape[1]

    idf = np.log(num_documents/tdm_.sum(axis=1))
    return (tdm_.T * idf).T
