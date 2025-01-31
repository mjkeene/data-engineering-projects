<h3>Simple ETL pipeline: CSV to SQLite</h3>

Build a pipeline that:

1. <b>Extracts</b> data from a CSV file.
2. <b>Transforms</b> the data by cleaning or modifying it.
3. <b>Loads</b> the data into a SQLite database.

<h4>Steps to Build:</h4>

1. Data Extraction:

   * Use a publicly available dataset (e.g., a CSV from Kaggle or data.gov).
   * I used [this movie dataset](https://www.kaggle.com/datasets/utkarshx27/movies-dataset) from Kaggle.


2. Data Transformation:

* Use pandas to:

  * Handle missing values (e.g., fill with defaults or drop rows).
  * Normalize the genre column to lowercase.
  * Filter rows based on certain conditions (e.g., rating > 5).
  * Add a calculated field (e.g., decade from release_year).

3. Data Loading:


* Use SQLite (built into Python) to:

  * Create a database and a table schema.
  * Load the cleaned data into the table.
  * Run a basic SQL query to verify the data was loaded correctly.


<h4>Repository Structure</h4>

```
csv_to_sqlite_data_pipeline/
│
├── data/
│   ├── movies.csv         # Source data (CSV)
├── src/
│   ├── etl_pipeline.py    # Main ETL script
│── notebooks/
│   ├── exploratory_data_analysis.ipynb
├── tests/
│   ├── test_etl.py        # Optional: Basic tests for transformations
├── requirements.txt       # Python dependencies (e.g., pandas, sqlite3)
├── README.md              # Project documentation
└── LICENSE                # Open-source license
```
