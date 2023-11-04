import nltk
import os
import django
from django.utils import timezone
from tdm.pushFunctions import overviewList, contentsList
from tdm.models import Documents
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "textIrApp.settings")
django.setup()


# get document titles
documentTitles = [title.split('.')[0]
                  for title in nltk.corpus.gutenberg.fileids()]

# get a list of document overviews
documentOverviews = overviewList(fileDirectory="gutenberg")

# get contents of a document
documetContents = contentsList(fileDirectory_="gutenberg")

# Iterate through the lists and create instances of the Documents model
for i in range(len(documentTitles)):
    document = Documents(
        title=documentTitles[i],
        overview=documentOverviews[i],
        content=documetContents[i],
        date_created=timezone.now()
    )
    document.save()

print("Data pushed to the database successfully.")
