## Improved Information Retrieval with Postgre SQL

Retrieving documents based solely on query terms is slow and not scalable. Moreover, it is usually needed in information retrieval systems to arrange query results based on order of relevance.  

This project aims to optimize the speed of document retrieval and ensure the display of retrieved documents in order of relevance. This will significantly impact the responsiveness requirement of end-user applications, particularly web apps, where presenting results within a 2-second timeframe is crucial.


The current implementation approach is to use PostgreSQL with Django framework, Python text processing libraries for data cleaning, using term-frequency (tf-idf) or Postgre's ts-rank for document ranking. A dictionary data structure or hashing can be used to index query terms to documents for improved performance.
