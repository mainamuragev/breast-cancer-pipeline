import pandas as pd

df = pd.read_csv('/home/mainavm/breast_cancer_pipeline/diagnostic_data.csv')
print("🧠 Columns in CSV:", df.columns.tolist())
