import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pandas as pd
import pytest
from src.etl_pipeline import extract, load
import sqlite3


@pytest.fixture
def valid_csv_file(tmp_path):
    """
    Fixture to create a temporary valid CSV file.
    """
    file_path = tmp_path / "valid_movie_dataset.csv"
    data = {
        "index": [1, 2],
        "budget": [100000, 200000],
        "genres": ["Action", "Comedy"],
        "title": ["Movie A", "Movie B"]
    }
    pd.DataFrame(data).to_csv(file_path, index=False)
    return file_path


@pytest.fixture
def empty_csv_file(tmp_path):
    """
    Fixture to create an empty CSV file.
    """
    file_path = tmp_path / "empty_movie_dataset.csv"
    open(file_path, "w").close()  # Create an empty file
    return file_path


@pytest.fixture
def invalid_csv_file(tmp_path):
    """
    Fixture to create a file with invalid content (not a proper CSV).
    """
    file_path = tmp_path / "invalid_movie_dataset.txt"
    file_path.write_text("This is not a valid CSV file.")
    return file_path


def test_extract_valid_csv(valid_csv_file):
    """
    Test the extract function with a valid CSV file.
    """
    df = extract(valid_csv_file)
    assert not df.empty
    assert len(df) == 2
    assert "title" in df.columns


def test_extract_missing_file():
    """
    Test the extract function with a missing file.
    """
    with pytest.raises(FileNotFoundError):
        extract("non_existent_file.csv")


def test_extract_empty_csv(empty_csv_file):
    """
    Test the extract function with an empty CSV file.
    """
    with pytest.raises(pd.errors.EmptyDataError):
        extract(empty_csv_file)


def test_extract_invalid_file_format(invalid_csv_file):
    """
    Test the extract function with a non-CSV file.
    """
    with pytest.raises(pd.errors.ParserError):
        extract(invalid_csv_file)


def test_load_data_into_sqlite(valid_csv_file):
    """
    Test loading the data into SQLite.
    """
    df = extract(valid_csv_file)
    load(df, "test_sqlite_db", "movies")

    # Verify that the data is correctly inserted into the SQLite database
    conn = sqlite3.connect("test_sqlite_db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM movies")
    row_count = cursor.fetchone()[0]
    assert row_count == len(df)
    conn.close()
