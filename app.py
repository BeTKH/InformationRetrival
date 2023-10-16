# app.py
import psycopg2

# Database connection parameters
db_params = {
    "dbname": "mydb",
    "user": "myuser",
    "password": "mypassword",
    "host": "db",  # This is the name of the PostgreSQL service in Docker Compose
    "port": "5432",
}

# Connect to the database
try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    print(f"Connected to PostgreSQL: {cursor.fetchone()}")
    conn.close()
except Exception as e:
    print(f"Error: {e}")
