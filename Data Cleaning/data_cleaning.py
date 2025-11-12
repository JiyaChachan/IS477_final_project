"""
data_cleaning.py
 - reads raw Airbnb gzip CSV
 - keeps columns id, latitude, longitude, price
 - cleans price and converts to float
 - writes cleaned CSV gz for downstream use
"""

import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/airbnb_listings_los-angeles_2025-09-01.csv.gz")
OUT_DIR = Path("data/processed")
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_PATH = OUT_DIR / "airbnb_clean.csv.gz"

# Load raw Airbnb (compressed)
airbnb = pd.read_csv(RAW_PATH, compression="gzip", low_memory=False)

airbnb = airbnb[['id', 'latitude', 'longitude', 'price']]
airbnb['price'] = airbnb['price'].replace('[\$,]', '', regex=True).astype(float)
airbnb

# Save cleaned data
airbnb.to_csv(OUT_PATH, index=False, compression="gzip")
print(f"Saved cleaned Airbnb data to: {OUT_PATH}")
