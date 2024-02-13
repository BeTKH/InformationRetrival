import psycopg2
from readContents import getDocTitles, getOverviews, getContents


# setup db connection
conn = psycopg2.connect(
    dbname="irDB",
    user="bekal",
    password="1433",
    host="localhost",
    port="5432"
)

# get file names

fileDir_ = 'gutenberg'

titles = getDocTitles()
overviews = getOverviews(fileDir_)
contents = getContents(fileDir_)

# Create a cursor object using the connection
cur = conn.cursor()

# SQL statement for data insertion into table 'tdm_document'
sql = "INSERT INTO tdm_document  (title, overview, content) VALUES (%s, %s, %s)"

# Execute the SQL statement for each tuple in the list
for title, overview, content in zip(titles, overviews, contents):
    data = (title, overview, content)
    cur.execute(sql, data)

    # Commit the transaction and close the cursor and connection
conn.commit()
cur.close()
conn.close()
