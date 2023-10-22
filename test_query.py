import psycopg2

# Define the connection parameters





try:
    
    # Establish a connection to the PostgreSQL database ( installed locally)
    conn = psycopg2.connect(
    dbname="loan_status",
    user="postgres",
    password="1433",
    host="localhost",
    port="5432")
   
    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Define your SQL query: loan_data_woc is a table under loan_status databse 
    query = "SELECT Loan_ID, Gender, Property_Area \
             FROM loan_data_woc \
             WHERE Property_Area ='Rural' AND Gender = 'Female' AND Education ='Graduate';"

    # Execute the SQL query
    cursor.execute(query)

    # Fetch the results
    results = cursor.fetchall()

    # Do something with the results (e.g., print them)

    print('\nLoan_ID, Gender, Property_Area \n')
    for row in results:
        print(row)

except psycopg2.Error as e:
    print("Error connecting to the database:", e)

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()
