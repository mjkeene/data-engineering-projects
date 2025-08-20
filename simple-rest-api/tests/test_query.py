import pandas as pd
import pytest
from lambda_core.query import load_data_from_s3

# For testing, we'll read a local CSV instead of S3
TEST_CSV = "sample_data/employees_15.csv"

def test_load_csv_local():
    df = pd.read_csv(TEST_CSV, parse_dates=["date_joined"])
    
    # Basic checks
    assert not df.empty, "DataFrame should not be empty"
    assert "employee_id" in df.columns
    assert "name" in df.columns
    assert "salary" in df.columns
    assert df.shape[0] == 15, "Should have 15 rows"

def test_query_loader_monkeypatch(monkeypatch):
    """Monkeypatch boto3 S3 client to return local CSV bytes."""
    import io
    class FakeS3Client:
        def get_object(self, Bucket, Key):
            with open(TEST_CSV, "rb") as f:
                return {"Body": io.BytesIO(f.read())}
    
    monkeypatch.setattr("lambda_core.query.s3_client", FakeS3Client())
    
    df = load_data_from_s3("fake-bucket", "fake-key.csv")
    assert df.shape[0] == 15
    assert "department" in df.columns
