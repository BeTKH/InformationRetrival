import psycopg2

# Define the connection parameters

#the host is -> postgres-docker IP address: 172.17.0.2

db_params = {
    'host': '172.17.0.2',        # Use 'localhost' because the database is running in a Docker container on your local machine.
    'port': 1652,               # The port mapped to the container.
    'database': 'postgres',   # Replace with your database name.
    'user': 'postgres',         # The PostgreSQL superuser.
    'password': '1433'  # The password you set when starting the container.
}


try:
    # Connect to the PostgreSQL server
    conn = psycopg2.connect(**db_params)
   
    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Define your SQL query
    query = "SELECT * FROM ndsu;"

    # Execute the SQL query
    cursor.execute(query)

    # Fetch the results
    results = cursor.fetchall()

    # Do something with the results (e.g., print them)
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
