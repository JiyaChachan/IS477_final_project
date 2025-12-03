# Data Acquisition & Verification

This project uses three publicly available datasets:  
- **Inside Airbnb (Los Angeles)**  
- **Zillow Home Value Index (ZHVI)**  
- **U.S. Census Bureau TIGER/Line ZIP Code Tabulation Areas (ZCTA)**  

Each dataset is acquired using a reproducible Python script.  
This README describes how others can re-acquire these data and verify file integrity with checksums.

---

## 1. Inside Airbnb – Los Angeles Listings

**Dataset:** Inside Airbnb (Los Angeles)  
**Access Method:** HTTPS download (compressed `.csv.gz` file)  
**Source URL:**  
[https://data.insideairbnb.com/united-states/ca/los-angeles/2025-09-01/data/listings.csv.gz](https://data.insideairbnb.com/united-states/ca/los-angeles/2025-09-01/data/listings.csv.gz)

**Script:** `download_airbnb_data.py`  
**Output File:** `data/raw/airbnb_listings-los-angeles_2025-09-01.csv.gz`

**Description:**  
This dataset contains detailed listing-level information for Los Angeles, including host IDs, property type, geographic coordinates, nightly price, and availability metrics.  
It is used to measure the density of Airbnb listings per ZIP code and analyze their potential relationship with local housing prices.

---

## Steps to Acquire the Dataset

1. Ensure you have Python 3.8+ and the required libraries installed:
   ```bash
   pip install requests pandas

2. Run the acquisition script:
   ```bash
   python download_airbnb_data.py

3. The script will download the dataset from Inside Airbnb and save it to data/raw/airbnb_listings-los-angeles_2025-09-01.csv.gz

## Checksum Verification

To ensure reproducibility, verify the SHA-256 checksum after download.

Expected Checksum: 
```bash
ee8673930b70c6563f7ad42f90fa02595ee495bd0e9c2a6186ad310442cab024
```

To Verify (Linux/macOS/Git Bash):
```bash
!sha256sum data/raw/airbnb_listings-los-angeles_2025-09-01.csv.gz
```
If the hash output matches the value above, the dataset is identical to the version used in this project.


---

## 2. Zillow – ZIP-Level Home Value Index (ZHVI)

**Dataset:** Zillow Home Value Index (ZHVI)
**Access Method:** HTTPS download (CSV)
**Source URL:**
[https://files.zillowstatic.com/research/public_csvs/zhvi/Zip_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv](https://files.zillowstatic.com/research/public_csvs/zhvi/Zip_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv)

**Script:** `download_zillow_data.py`
**Output File:** `data/raw/zillow_zip_zhvi_2025.csv`

**Description:**
This dataset provides monthly home value data at the ZIP-code level across the U.S.
It includes smoothed, seasonally adjusted estimates of typical home values (ZHVI) and is used to assess trends in housing affordability and market variation across ZIP codes.

---

### Steps to Acquire the Dataset

1. Ensure you have Python 3.8+ and the required libraries installed:

   ```bash
   pip install requests pandas
   ```

2. Run the acquisition script:

   ```bash
   python download_zillow_data.py
   ```

3. The script will download the dataset from Zillow Research and save it to:

   ```
   data/raw/zillow_zip_zhvi_2025.csv
   ```

---

### Checksum Verification

To ensure reproducibility, verify the SHA-256 checksum after download.

**Expected Checksum:**

```bash
a90fd263c61a81aac1837607501b38f16adc8e9e33a0cb5f683842e0bd7ff63b
```

**To Verify (Linux/macOS/Git Bash):**

```bash
!sha256sum data/raw/zillow_zip_zhvi_2025.csv
```

If the hash output matches the value above, the dataset is identical to the version used in this project.

---

## 3. U.S. Census Bureau – TIGER/Line ZCTA (2025)

**Dataset:** ZIP Code Tabulation Areas (ZCTA) – 2025
**Access Method:** HTTPS download (ZIP archive containing shapefiles)
**Source URL:**
[https://www2.census.gov/geo/tiger/TIGER2025/ZCTA520/tl_2025_us_zcta520.zip](https://www2.census.gov/geo/tiger/TIGER2025/ZCTA520/tl_2025_us_zcta520.zip)

**Script:** `download_census_zcta_data.py`
**Output Directory:** `data/raw/zcta2025/`

**Description:**
The U.S. Census Bureau TIGER/Line ZCTA shapefiles define ZIP Code boundaries used for spatial analysis.
These files are used to align Airbnb and Zillow datasets geographically at the ZIP code level.

---

### Steps to Acquire the Dataset

1. Ensure you have Python 3.8+ and the required libraries installed:

   ```bash
   pip install requests zipfile36 geopandas
   ```

2. Run the acquisition script:

   ```bash
   python download_census_zcta_data.py
   ```

3. The script will download and extract the shapefile bundle into:

   ```
   data/raw/zcta2025/
   ```

---

### Checksum Verification

To ensure reproducibility, verify the SHA-256 checksum after download.

**Expected Checksum:**

```bash
3a701eebdf9982269f87aa19c49ccc6596ca303126e4901dd2ee814f22a591b4
```

**To Verify (Linux/macOS/Git Bash):**

```bash
!sha256sum data/raw/zcta2025/tl_2025_us_zcta520.shp
```

If the hash output matches the value above, the dataset is identical to the version used in this project.
