from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
import os

app = FastAPI()

@app.get("/risk-scores")
def get_risk_scores():
    path = "/opt/airflow/data/scored_output.csv"
    if not os.path.exists(path):
        return JSONResponse(content={"error": "Risk scores not found"}, status_code=404)

    df = pd.read_csv(path)
    return df.to_dict(orient="records")

