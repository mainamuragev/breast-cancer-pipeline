import pandas as pd
import psycopg2

# ✅ Define correct column names manually
columns = [
    'id', 'diagnosis', 'mean_radius', 'mean_texture', 'mean_perimeter', 'mean_area',
    'mean_smoothness', 'mean_compactness', 'mean_concavity', 'mean_concave_points',
    'mean_symmetry', 'mean_fractal_dimension', 'radius_se', 'texture_se', 'perimeter_se',
    'area_se', 'smoothness_se', 'compactness_se', 'concavity_se', 'concave_points_se',
    'symmetry_se', 'fractal_dimension_se', 'worst_radius', 'worst_texture', 'worst_perimeter',
    'worst_area', 'worst_smoothness', 'worst_compactness', 'worst_concavity',
    'worst_concave_points', 'worst_symmetry', 'worst_fractal_dimension'
]

# ✅ Load CSV with no header and assign column names
df = pd.read_csv('diagnostic_data.csv', header=None, names=columns)

# ✅ Add default recurrence column
df['recurrence'] = 'unknown'

# Normalize column names
df.columns = df.columns.str.strip().str.lower()

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname='mydatabase',
    user='postgres',
    password='mainamurage',
    host='localhost',
    port='5432'
)
cursor = conn.cursor()

# Insert each row with debug print
for _, row in df.iterrows():
    print("🚀 Inserting row:", row[['mean_radius', 'mean_texture', 'mean_perimeter', 'mean_area', 'recurrence']].to_dict())
    try:
        cursor.execute("""
            INSERT INTO diagnostics (mean_radius, mean_texture, mean_perimeter, mean_area, recurrence)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            row['mean_radius'],
            row['mean_texture'],
            row['mean_perimeter'],
            row['mean_area'],
            row['recurrence']
        ))
    except Exception as e:
        print("❌ Failed to insert row:", row.to_dict())
        print("Error:", e)

conn.commit()
cursor.close()
conn.close()
print("✅ Data ingestion complete.")
