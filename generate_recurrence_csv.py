import pandas as pd
import random
import os

recurrence_types = ['local', 'regional', 'distant']
data = []

for i in range(100):
    patient_id = f'P{i:04d}'
    if random.random() < 0.3:
        recurrence_type = random.choice(recurrence_types)
        days = random.randint(180, 1200)
        data.append({
            'patient_id': patient_id,
            'recurrence_type': recurrence_type,
            'days_since_diagnosis': days,
            'recurrence_confirmed': True,
            'notes': ''
        })

df = pd.DataFrame(data)
os.makedirs("recurrence_env", exist_ok=True)
df.to_csv("recurrence_env/recurrence_events.csv", index=False)
print("recurrence_events.csv created successfully.")
