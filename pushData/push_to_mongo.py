from pymongo import MongoClient
from getContents import *

# MongoDB connection setup
client = MongoClient('localhost', 27017)  # Connect to the MongoDB instance
# Use or create a database named 'gutenbergDatabase'
db = client['irDB']
# Use or create a collection named 'gutenbergCollections'
collection = db['gutenbergFiles']

# Get file names
fileDir_ = 'gutenberg'
titles = getDocTitles()
overviews = getOverviews(fileDir_)
contents = getContents(fileDir_)


# Insert data into MongoDB collection
for title, overview, content in zip(titles, overviews, contents):
    file_data = {
        'title': title,
        'overview': overview,
        'content': content
    }
    collection.insert_one(file_data)

client.close()  # Close the connection
