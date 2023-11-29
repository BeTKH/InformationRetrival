import os
import nltk


# get document title
def getDocTitles():
    return [title.split('.')[0] for title in nltk.corpus.gutenberg.fileids()]


# get document overviews
def getOverviews(fileDirectory):

    fileNames = nltk.corpus.gutenberg.fileids()
    overviews = []
    for file_name in fileNames:
        file_path = os.path.join(fileDirectory, file_name)
        if os.path.isfile(file_path):
            try:
                with open(file_path, "r", encoding='latin-1') as file:
                    content = file.read(100)
                    overviews.append(content)
            except Exception as e:
                print(f"Error reading {file_name}: {e}")
                continue

    return overviews


# get document contents
def getContents(fileDirectory):

    fileNames = nltk.corpus.gutenberg.fileids()

    content_list = []
    for file_name in fileNames:
        file_path = os.path.join(fileDirectory, file_name)
        if os.path.isfile(file_path):
            try:
                with open(file_path, "r", encoding='latin-1') as file:
                    content = file.read()
                    content_list.append(content)
            except Exception as e:
                print(f"Error reading {file_name}: {e}")
                continue

    return content_list
