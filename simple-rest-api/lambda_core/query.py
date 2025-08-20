import pandas as pd
import boto3
from io import BytesIO

s3_client = boto3.client("s3")

def load_data_from_s3(bucket: str, key: str) -> pd.DataFrame:
    """Load CSV or Parquet from S3 into a DataFrame."""

    obj = s3_client.get_object(Bucket=bucket, Key=key)
    data_bytes = obj['Body'].read()
    
    if key.endswith(".csv"):
        df = pd.read_csv(BytesIO(data_bytes), parse_dates=["date_joined"])
    elif key.endswith(".parquet"):
        df = pd.read_parquet(BytesIO(data_bytes))
    else:
        raise ValueError("Unsupported file type")
    return df
