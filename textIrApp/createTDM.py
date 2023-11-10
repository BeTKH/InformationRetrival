from .customLibraries import *


# load files
corpus = load_allfiles()


# clean all collection of files ( corpus)
cleanCorp = clean_Files(corpus)

# create term docment matrix using clean data
tdm, allTerms = create_term_document_matrix(cleanCorp)


# tdm log scaled
tdm_tf = logScale_tf(tdm)

# tdm tf_idf
tdm_tfidf = scale_tfidf(tdm)
