## Information Retrieval WebApp (Postgre SQL + Django)

### Problem:

- Retrieving documents by looking for query terms alone throughout documents is slow and not scalable. Moreover, it is usually needed in information retrieval systems to arrange query results based on the order of relevance to the query.

### Accomplishments:

- Implemented a responsive information retrieval WebApp (< 2 sec) using PostgreSQL + Django
- vectorial representation of files using a term-document-matrix (TDM) and query results
- Retrieval of those documents using a dictionary data structure and display of search result files in order of relevance.
- Created a database schema in PostgreSQL with Python's Django models.
- Database connection, configuration, and population with text files.
- Text pre-processing and cleaning using natural language processing toolkit ( NLTK)

View the Jupyter Notebook [here.](https://htmlpreview.github.io/?https://github.com/BeTKH/ir_notebook/blob/main/IR_final.html)

## How to run the app

- Create a `pipenv` virtual environment first using [documentation](https://pipenv.pypa.io/en/latest/installation.html)

- Install dependencies from Pipfile

  ```
  pipenv install
  ```

- To install exact versions run:

  ```
  pipenv install --ignore-pipfile
  ```

- run the app:
  ```
  python manage.py runserver
  ```

### Video

https://github.com/BeTKH/IR_postgres/assets/45674779/5944657a-e4e5-4f7d-9761-980ff171d0a4

## System Architecture

<img width="1346" alt="Screenshot 2024-01-29 at 3 55 10 PM" src="https://github.com/BeTKH/IR_postgres/assets/45674779/22987fb2-b913-40f6-a274-90f05d45a046">

## Term-Document Matrix

<img width="766" alt="Screenshot 2024-01-29 at 3 49 27 PM" src="https://github.com/BeTKH/IR_postgres/assets/45674779/c856f793-bb1e-493f-8bba-955e3da3529b">

## Query processing

![newplot (4)](https://github.com/BeTKH/IR_postgres/assets/45674779/2f934678-b054-40b4-a93c-c9f876da44d7)

## Zif's Law

![newplot (1)](https://github.com/BeTKH/IR_postgres/assets/45674779/975b7ac2-18fe-4d06-ac9f-3bbdfde4912b)

## Web App's UI

<img width="1174" alt="Screenshot 2024-01-29 at 3 55 38 PM" src="https://github.com/BeTKH/IR_postgres/assets/45674779/e5cc53ce-f462-4c89-9015-05ecd3c043b2">
