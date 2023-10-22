# app.py
import psycopg2

# Database connection parameters
db_params = {
    "dbname": "loan_status",
    "user": "postgres",
    "password": "1433",
    "host": "localhost",  # This is the name of the PostgreSQL service in Docker Compose
    "port": "5432",
}

# Connect to the database
try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    print(f"Connected to PostgreSQL: {cursor.fetchone()}")
    print("\n\nconnection is successful!!!")
    conn.close()
except Exception as e:
    print(f"Error: {e}")
