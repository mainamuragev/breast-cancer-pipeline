import psycopg2
import pandas as pd

# Connect to PostgreSQL exposed on localhost
conn = psycopg2.connect(
    host='localhost',
    dbname='airflow',
    user='airflow',
    password='airflow'
)

# Query the recurrence_events table
query = "SELECT * FROM recurrence_events"
df = pd.read_sql(query, conn)
conn.close()

# Print the first few rows
print("\n✅ Recurrence Events Preview:\n")
print(df.head())
