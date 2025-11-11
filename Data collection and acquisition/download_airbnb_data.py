"""
download_airbnb_data.py
-----------------------
Data Collection Script: Inside Airbnb (Los Angeles)
Purpose:
    - Programmatically download Airbnb listing data
    - Handle compressed files (.gz)
    - Provide reproducible, dated snapshot
"""
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import requests, zipfile, io, os
import numpy as np
from pathlib import Path

URL = "https://data.insideairbnb.com/united-states/ca/los-angeles/2025-09-01/data/listings.csv.gz"
OUTPUT_PATH = Path("data/raw/airbnb_listings_los-angeles_2025-09-01.csv.gz")
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; DataCollector/1.0)"}

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

print("Downloading Inside Airbnb dataset for Los Angeles (2025-09-01)...")

response = requests.get(URL, headers=HEADERS, timeout=60)
response.raise_for_status()
with open(OUTPUT_PATH, "wb") as f:
    f.write(response.content)
print(f"Download complete: {OUTPUT_PATH}")

airbnb = pd.read_csv(OUTPUT_PATH, compression="gzip", low_memory=False)
print(f"File loaded successfully! Shape: {airbnb.shape}")
airbnb.head(3)
