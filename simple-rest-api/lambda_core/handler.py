import json
from query import load_data_from_s3

def lambda_handler(event, context):
    """
    Lambda handler that returns all rows from a CSV or Parquet in S3.
    Expects query parameters: bucket, key
    """
    params = event.get("queryStringParameters", {}) or {}

    bucket = params.get("bucket")
    key = params.get("key")
    if not bucket or not key:
        return {"statusCode": 400, "body": json.dumps({"error": "bucket and key required"})}

    # Load data
    df = load_data_from_s3(bucket, key)

    # Convert to JSON
    result = df.to_dict(orient="records")

    return {
        "statusCode": 200,
        "body": json.dumps(result, default=str),
        "headers": {"Content-Type": "application/json"}
    }
