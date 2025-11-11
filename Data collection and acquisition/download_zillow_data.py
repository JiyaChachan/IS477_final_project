"""
download_zillow_data.py
-----------------------
Data Collection Script: Zillow Home Value Index (ZHVI)
Purpose:
    - Programmatically download ZIP-level housing price data
    - Use Zillow's public research dataset
    - Store reproducible snapshot (dated URL)
"""

import requests
import pandas as pd
from pathlib import Path

URL = "https://files.zillowstatic.com/research/public_csvs/zhvi/Zip_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv?t=1762838443"
OUTPUT_PATH = Path("data/raw/zillow_zip_zhvi_2025.csv")
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; ZillowDataDownloader/1.0)"}

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

print("Downloading Zillow ZHVI (All Homes, ZIP-level)...")

response = requests.get(URL, headers=HEADERS, timeout=60)
response.raise_for_status()

with open(OUTPUT_PATH, "wb") as f:
    f.write(response.content)

print(f"Download complete: {OUTPUT_PATH}")

zillow = pd.read_csv(OUTPUT_PATH, low_memory=False)
print(f"File loaded successfully! Shape: {zillow.shape}")
zillow.head(3)
