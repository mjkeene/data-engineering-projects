import pandas as pd
import os
import sqlite3

def extract(file_path: str) -> pd.DataFrame:
    """
    Extract data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Extracted data as a Pandas DataFrame.
    """
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file at {file_path} does not exist.")

        # Check for file extension to ensure it's a CSV file
        if not str(file_path).lower().endswith('.csv'):
            raise pd.errors.ParserError(f"The file '{file_path}' is not a valid CSV file.")

        # Read the CSV file
        print(f"Extracting data from {file_path}...")
        df = pd.read_csv(file_path)
        rows, cols = df.shape
        print(f"Data extraction completed. {rows} rows loaded, {cols} cols loaded.")
        # Return an empty DataFrame if the file has no data
        if df.empty:
            print("Warning: The CSV file is empty.")
        return df

    except FileNotFoundError as e:
        print(f"Error: The file '{file_path}' was not found.")
        raise e
    except pd.errors.EmptyDataError as e:
        print(f"Error: The file '{file_path}' is empty.")
        raise e
    except pd.errors.ParserError as e:
        print(f"Error: The file '{file_path}' could not be parsed.")
        raise e
    except UnicodeDecodeError as e:
        print(f"Error: The file '{file_path}' contains invalid characters or format.")
        raise pd.errors.ParserError("File contains invalid format or characters.")


def transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform the data by cleaning and enriching it.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: Transformed DataFrame.
    """
    print("Starting data transformation...")

    # Example transformations
    df = df.dropna(subset=["budget", "revenue"])  # Remove rows with missing budget or revenue
    df["budget"] = df["budget"].astype(float)
    df["revenue"] = df["revenue"].astype(float)

    # Calculate ROI (Return on Investment)
    df["roi"] = (df["revenue"] - df["budget"]) / df["budget"]

    # Convert release_date to datetime and extract release_year
    df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
    df["release_year"] = df["release_date"].dt.year

    print(f"Transformation completed. {len(df)} rows remain after cleaning.")
    return df


def load(df: pd.DataFrame, db_name: str, table_name: str) -> None:
    """
    Load the transformed data into a SQLite database.

    Args:
        df (pd.DataFrame): The DataFrame to load.
        db_name (str): The name of the database.
        table_name (str): The name of the table.

    """
    try:
        # Connect to SQLite database
        conn = sqlite3.connect(db_name)
        # write the df to the specified table (if it doesn't exist, it will be created)
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"Data loaded into table '{table_name}' in database '{db_name}'.")
    except Exception as e:
        print(f"Error: Could not load data into SQLite database. {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    # Get the root directory of the project
    root_dir = os.path.dirname(os.path.abspath(__file__))

    # Move one directory up to reach project root
    project_root = os.path.abspath(os.path.join(root_dir, ".."))

    input_file = os.path.join(project_root, "data", "movie_dataset.csv")  # Input dataset
    output_file = os.path.join(project_root, "data", "movies_transformed.csv")

    # Run the ETL pipeline
    try:
        raw_data = extract(input_file)
        transformed_data = transform(raw_data)
        load(transformed_data, output_file)
    except Exception as e:
        print(f"An error occurred: {e}")
