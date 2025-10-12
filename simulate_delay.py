import psycopg2
import pandas as pd

# Connect to PostgreSQL
print("Connecting to cancer_db as airflow...")
conn = psycopg2.connect(
    host='localhost',
    dbname='cancer_db',
    user='airflow',
    password='airflow'
)

# Query recurrence events from the public schema
query = "SELECT * FROM public.recurrence_events"
df = pd.read_sql(query, conn)

# Check if data was loaded
print("Rows loaded:", len(df))
if df.empty:
    print("⚠️ No recurrence events found in the database.")
    exit()

# Simulate delay logic
def get_delay(row):
    confirmed = row['recurrence_confirmed']
    rtype = row['recurrence_type']
    if confirmed:
        return 0
    elif rtype == 'Local':
        return 3
    elif rtype == 'Regional':
        return 7
    elif rtype == 'Distant':
        return 5
    else:
        return 2

# Apply delay logic
df['delay_days'] = df.apply(get_delay, axis=1)
df['delayed_day_count'] = df['days_since_diagnosis'] + df['delay_days']

# Preview results
print("\n🔁 Recurrence Delay Simulation:\n")
print(df[['patient_id', 'recurrence_type', 'recurrence_confirmed', 'days_since_diagnosis', 'delay_days', 'delayed_day_count']].head())

# Export to CSV
df.to_csv("recurrence_delay.csv", index=False)
