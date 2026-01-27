import pandas as pd
from sqlalchemy import create_engine
import os

# Database connection
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

# Load taxi_zone_lookup.csv
def load_taxi_zone_lookup():
    if os.path.exists('taxi_zone_lookup.csv'):
        print('Loading taxi_zone_lookup.csv...')
        df_zones = pd.read_csv('taxi_zone_lookup.csv')
        df_zones.to_sql('taxi_zone_lookup', con=engine, if_exists='replace', index=False)
        print('Loaded taxi_zone_lookup.csv into taxi_zone_lookup table.')
    else:
        print('taxi_zone_lookup.csv not found.')

# Load green trip data (CSV or Parquet)
def load_green_trip_data():
    # Try CSV first, then Parquet
    green_csv = None
    green_parquet = None
    for f in os.listdir('.'):
        if f.startswith('green_tripdata') and f.endswith('.csv'):
            green_csv = f
        if f.startswith('green_tripdata') and f.endswith('.parquet'):
            green_parquet = f
    if green_csv:
        print(f'Loading {green_csv}...')
        df_green = pd.read_csv(green_csv)
        df_green.to_sql('green_taxi_data', con=engine, if_exists='replace', index=False)
        print(f'Loaded {green_csv} into green_taxi_data table.')
    elif green_parquet:
        print(f'Loading {green_parquet}...')
        df_green = pd.read_parquet(green_parquet)
        df_green.to_sql('green_taxi_data', con=engine, if_exists='replace', index=False)
        print(f'Loaded {green_parquet} into green_taxi_data table.')
    else:
        print('No green trip data file found.')

if __name__ == '__main__':
    load_taxi_zone_lookup()
    load_green_trip_data()
