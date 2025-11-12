#!/usr/bin/env python3
"""
data_integration.py
 - reads cleaned Airbnb
 - reads Zillow CSV
 - reads Census ZCTA shapefile
 - performs spatial join of Airbnb points to ZCTA
 - aggregates listings per ZIP, merges with Zillow latest column
 - classifies neighborhood_type and saves outputs
"""

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import numpy as np
from pathlib import Path

# Paths
AIRBNB_CLEAN = Path("data/processed/airbnb_clean.csv.gz")
ZILLOW_CSV = Path("data/raw/zillow_zip_zhvi_2025.csv")
ZCTA_SHP = Path("data/raw/zcta2025/tl_2025_us_zcta520.shp")  # expected location
OUT_DIR = Path("data/processed")
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_MERGED = OUT_DIR / "merged_airbnb_zillow_by_zip.csv"

# Load data
airbnb = pd.read_csv(AIRBNB_CLEAN, compression="gzip", low_memory=False)
zillow = pd.read_csv(ZILLOW_CSV, low_memory=False)
zcta = gpd.read_file(ZCTA_SHP).to_crs(epsg=4326)

# integration
zillow_la = zillow[(zillow['City'] == 'Los Angeles') & (zillow['StateName'] == 'CA')]
zillow_la

points = gpd.GeoDataFrame(
    airbnb,
    geometry=[Point(xy) for xy in zip(airbnb.longitude, airbnb.latitude)],
    crs='EPSG:4326'
)

joined = gpd.sjoin(points, zcta[['ZCTA5CE20', 'geometry']], how='left', predicate='within')
joined.rename(columns={'ZCTA5CE20': 'zipcode'}, inplace=True)
joined['zipcode'] = joined['zipcode'].astype(str).str.zfill(5)


airbnb_zip = joined.groupby('zipcode').agg(
    num_listings=('id', 'count'),
    avg_airbnb_price=('price', 'mean')
).reset_index()
airbnb_zip

latest_col = '2025-09-30'
zillow_subset = zillow_la[['RegionName', latest_col]].rename(columns={
    'RegionName': 'zipcode',
    latest_col: 'median_home_value'
})

# Ensure ZIPs are zero-padded
zillow_subset['zipcode'] = zillow_subset['zipcode'].astype(str).str.zfill(5)

# Merge
merged = airbnb_zip.merge(zillow_subset, on='zipcode', how='inner')

merged['neighborhood_type'] = np.where(
   (merged['num_listings'] > merged['num_listings'].median()),
    'Urban Core',
    'Suburban'
)

# Save merged result
merged.to_csv(OUT_MERGED, index=False)
print(f"Saved merged dataset to: {OUT_MERGED}")
