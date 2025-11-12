"""
download_census_zcta_data.py
----------------------------
Data Collection Script: U.S. Census Bureau ZCTA (ZIP Code Tabulation Areas)
Purpose:
    - Programmatically download TIGER/Line shapefiles for ZIP Code boundaries
    - Extract and store them for spatial joins (used to link ZIP codes to Airbnb listings)
"""
import requests
import pandas as pd
from pathlib import Path

URL = "https://www2.census.gov/geo/tiger/TIGER2025/ZCTA520/tl_2025_us_zcta520.zip"
OUT_DIR = Path("data/raw/zcta2025")
OUT_DIR.mkdir(parents=True, exist_ok=True)

print("Downloading U.S. Census TIGER/Line ZCTA shapefiles (2025)...")

response = requests.get(URL, timeout=60)
response.raise_for_status()

with zipfile.ZipFile(io.BytesIO(response.content)) as z:
    z.extractall(OUT_DIR)

print(f"Extracted files to: {OUT_DIR}")
print("Files:", [f.name for f in OUT_DIR.iterdir()])
zcta = gpd.read_file(os.path.join(OUT_DIR, "tl_2025_us_zcta520.shp")).to_crs(epsg=4326)
