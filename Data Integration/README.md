## Data Integration Documentation

**Script:** `data_integration.py`
**Purpose:** To spatially integrate Airbnb listing data with Zillow housing values using Census ZIP Code Tabulation Area (ZCTA) boundaries.
**Output:** `data/processed/merged_airbnb_zillow_by_zip.csv`

---

### **Overview**

The `data_integration.py` script combines three cleaned datasets — **Inside Airbnb (Los Angeles)**, **Zillow Home Value Index (ZHVI)**, and **U.S. Census Bureau ZCTA shapefiles** — to analyze the relationship between Airbnb listing density and housing prices across ZIP codes.
The script uses geographic data joins and simple aggregation to align all datasets at the ZIP code level.

---

### **Integration Steps**

1. **Load Data Sources**

   * The script reads:

     * Cleaned Airbnb listings (`data/processed/airbnb_clean.csv.gz`)
     * Zillow ZHVI ZIP-level dataset (`data/raw/zillow_zip_zhvi_2025.csv`)
     * U.S. Census ZCTA shapefile (`data/raw/zcta2025/tl_2025_us_zcta520.shp`)
   * All datasets are loaded into pandas or GeoPandas DataFrames.
   * The shapefile is converted to the WGS84 coordinate system (EPSG:4326) for spatial compatibility.

2. **Subset Zillow to Los Angeles**

   * Zillow data is filtered to include only rows where:

     ```python
     (zillow['City'] == 'Los Angeles') & (zillow['StateName'] == 'CA')
     ```
   * This ensures that only ZIP codes within Los Angeles County are retained for analysis.

3. **Convert Airbnb Listings to Geospatial Points**

   * Each Airbnb listing’s latitude and longitude are converted into geographic point geometries using:

     ```python
     geometry=[Point(xy) for xy in zip(airbnb.longitude, airbnb.latitude)]
     ```
   * These points are stored in a GeoDataFrame (`points`) with CRS set to EPSG:4326.

4. **Spatial Join: Airbnb → ZCTA**

   * A spatial join assigns each Airbnb listing to the corresponding ZIP Code Tabulation Area (ZCTA) polygon using:

     ```python
     gpd.sjoin(points, zcta[['ZCTA5CE20', 'geometry']], how='left', predicate='within')
     ```
   * The ZCTA code (`ZCTA5CE20`) is renamed to `zipcode` and zero-padded to five digits for consistency.

5. **Aggregate Airbnb Data by ZIP Code**

   * Listings are grouped by ZIP code to calculate:

     * `num_listings`: total number of Airbnb listings per ZIP
     * `avg_airbnb_price`: average nightly price per ZIP

     ```python
     airbnb_zip = joined.groupby('zipcode').agg(
         num_listings=('id', 'count'),
         avg_airbnb_price=('price', 'mean')
     ).reset_index()
     ```

6. **Prepare Zillow Subset**

   * The latest available home value column (`2025-09-30`) is selected and renamed for clarity:

     ```python
     zillow_subset = zillow_la[['RegionName', '2025-09-30']].rename(
         columns={'RegionName': 'zipcode', '2025-09-30': 'median_home_value'}
     )
     ```
   * ZIP codes are also zero-padded to ensure consistent formatting before merging.

7. **Merge Airbnb and Zillow Data**

   * The aggregated Airbnb ZIP-level summary is merged with Zillow home values:

     ```python
     merged = airbnb_zip.merge(zillow_subset, on='zipcode', how='inner')
     ```
   * This creates a unified dataset linking Airbnb activity to local housing values by ZIP.

8. **Neighborhood Classification**

   * Each ZIP code is classified into one of two neighborhood categories based on listing density:

     * **Urban Core** – ZIP codes with above-median Airbnb listing counts
     * **Suburban** – ZIP codes with below-median listing counts

     ```python
     merged['neighborhood_type'] = np.where(
         merged['num_listings'] > merged['num_listings'].median(),
         'Urban Core',
         'Suburban'
     )
     ```

9. **Save Integrated Dataset**

   * The final integrated dataset is saved to:

     ```
     data/processed/merged_airbnb_zillow_by_zip.csv
     ```
   * The file includes columns for:

     * `zipcode`
     * `num_listings`
     * `avg_airbnb_price`
     * `median_home_value`
     * `neighborhood_type`

---

### **Resulting Dataset Summary**

| Column Name         | Description                                |
| ------------------- | ------------------------------------------ |
| `zipcode`           | 5-digit ZIP Code Tabulation Area           |
| `num_listings`      | Number of Airbnb listings in that ZIP      |
| `avg_airbnb_price`  | Average Airbnb price in USD                |
| `median_home_value` | Zillow Home Value Index (ZHVI) for the ZIP |
| `neighborhood_type` | Classified as “Urban Core” or “Suburban”   |

---

### **Output Example**

```text
zipcode,num_listings,avg_airbnb_price,median_home_value,neighborhood_type
90001,22,135.67,540000,Suburban
90002,58,147.92,612000,Urban Core
90003,44,139.18,598000,Suburban
...
```

---

### **Summary**

This integration pipeline ensures that data from different sources (CSV, compressed CSV, and shapefile) are combined consistently using geographic boundaries.
The final dataset supports analysis of whether higher Airbnb activity correlates with increased housing costs across Los Angeles ZIP codes.
