import psycopg2

"""
Module to test database query
"""


try:
    
    # Establish a connection to the PostgreSQL database ( installed locally)
    connection = psycopg2.connect(
    dbname="loan_status",
    user="postgres",
    password="1433",
    host="localhost",
    port="5432")
   
    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Define your SQL query: loan_data_woc is a table under loan_status databse 
    query = "SELECT Loan_ID, Gender, Property_Area \
             FROM loan_data_woc \
             WHERE Property_Area ='Rural' AND Gender = 'Female' AND Education ='Graduate';"

    # Execute the SQL query
    cursor.execute(query)

    # Fetch the results
    records = cursor.fetchall()

    

    #print header of the table 
    print('\nLoan_ID, Gender, Property_Area \n')

    #print results iteratively
    for record in records:
        print(record)

except psycopg2.Error as e:
    print("Error connecting to the database:", e)

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
