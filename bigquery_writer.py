from google.cloud import bigquery
from datetime import datetime
import os

PROJECT_ID = "earnest-vine-463003-f1"
DATASET = "sports_model"
TABLE = "model_predictions"
TABLE_ID = f"{PROJECT_ID}.{DATASET}.{TABLE}"

def insert_prediction(payload):
    client = bigquery.Client(project=PROJECT_ID)

    if "generated_at" not in payload:
        payload["generated_at"] = datetime.utcnow()

    errors = client.insert_rows_json(TABLE_ID, [payload])
    if errors == []:
        print("✅ Prediction inserted successfully.")
    else:
        print("❌ Errors during insert:", errors)
    return errors