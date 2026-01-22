import pandas as pd
import sys

# Create a sample DataFrame
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print(df.head())

# Save DataFrame to a Parquet file with dynamic filename based on command-line argument
output_path = f"/app/output_day_{sys.argv[1]}.parquet"
print(f"Saving to {output_path}")
df.to_parquet(output_path)