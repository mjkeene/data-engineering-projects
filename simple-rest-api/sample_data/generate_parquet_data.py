import pandas as pd

# Read the existing CSV file
df = pd.read_csv("employees_15.csv")

# Save as Parquet
df.to_parquet("employees_15.parquet", engine="pyarrow", index=False)

print("Parquet file created: employees_15.parquet")
