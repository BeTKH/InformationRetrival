from .customLibraries import *


# load files
corpus = load_allfiles()


# clean all collection of files ( corpus)
cleanCorp = clean_Entirefiles(corpus)

# create term docment matrix using clean data
tdm, allTerms = create_term_document_matrix(cleanCorp)
