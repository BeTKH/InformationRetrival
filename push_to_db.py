import nltk
import psycopg2
from push_getContents import getDocTitles, getOverviews, getContents


# setup db connection
conn = psycopg2.connect(
    dbname="ir_test",
    user="kobro",
    password="1433",
    host="localhost",
    port="5432"
)

# get file names
fileNameList = nltk.corpus.gutenberg.fileids()
fileDir_ = 'gutenberg'

titles = getDocTitles()
overviews = getOverviews(fileNameList, fileDir_)
contents = getContents(fileNameList, fileDir_)

# Create a cursor object using the connection
cur = conn.cursor()

# SQL statement for data insertion into table 'tdm_documents '
sql = "INSERT INTO tdm_documents  (title, overview, content) VALUES (%s, %s, %s)"

# Execute the SQL statement for each tuple in the list
for title, overview, content in zip(titles, overviews, contents):
    data = (title, overview, content)
    cur.execute(sql, data)

    # Commit the transaction and close the cursor and connection
conn.commit()
cur.close()
conn.close()
