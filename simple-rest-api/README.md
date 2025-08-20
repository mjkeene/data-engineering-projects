# simple-rest-api

A lightweight Python package to expose CSV/Parquet data in S3 as a REST API via AWS Lambda + API Gateway. Supports dynamic query filtering on columns like dates, numeric values, and strings.

## Features

- Query CSV or Parquet files stored in S3
- Filter on multiple columns dynamically, e.g.:
  - `date_joined>2020-01-01`
  - `salary>50000`
  - `department=Engineering`
- Returns JSON results via Lambda + API Gateway

---

## Example API Request

If deployed on API Gateway, you can query the employee data like this:

```json
GET https://<api-id>.execute-api.<region>.amazonaws.com/prod/query?
bucket=my-bucket&
key=employees.csv&
salary=>50000&
date_joined>2020-01-01
```

## Project Structure
```bash
simple-rest-api/
│
├── lambda_core/ # Core Lambda code
│ ├── init.py
│ ├── handler.py # Lambda entry point
│ ├── query.py # Query/filter logic
│ ├── utils.py # Helpers (S3 loading, parsing, etc.)
│
├── sample_data/ # Example datasets for testing
│ ├── employees.csv
│ └── employees.parquet # Optional Parquet version
│
├── tests/ # Unit tests
│ ├── test_query.py
│
├── examples/ # Example scripts to demonstrate usage
│ └── run_local.py # Local testing script using lambda_service
│
├── requirements.txt # Python dependencies (pandas, boto3, etc.)
├── setup.py # Package setup for pip install
├── README.md # Overview, installation, usage
└── .gitignore # Ignore venv, pycache, etc.
```
