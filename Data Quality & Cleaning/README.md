# **Data Quality and Cleaning**

This document describes the steps used to **profile**, **evaluate**, and **clean** the Inside Airbnb dataset before integration with Zillow and Census ZCTA data.
All cleaning operations are implemented in the script:

```
data_cleaning.py
```
---

## **1. Data Profiling**

Before cleaning the Airbnb dataset, we performed basic data profiling to understand structure, content, and quality. Profiling focused on the following:

### **a. Structural Profiling**

We examined:

* number of rows and columns
* column names and types
* file format and compression

Commands used:

```python
airbnb.info()
airbnb.head()
```

**Findings:**

* The dataset contains many more columns than necessary for our analysis.
* Price values contained currency symbols and needed cleaning.

---

### **b. Content Profiling**

We explored:

* ranges and distributions of latitude, longitude, and prices
* presence of invalid or missing values

Commands used:

```python
airbnb['price'].isna().sum()
airbnb['price'].describe()
```

**Findings:**

* Several rows had missing or non-numeric `price` values.
* Latitude/longitude values contained proper coordinate formatting.
* Most columns were unrelated to our research question.

---

### **c. Quality Profiling Based on Data Quality Dimensions**

| Dimension        | What We Checked                            | Result                                                      |
| ---------------- | ------------------------------------------ | ----------------------------------------------------------- |
| **Accuracy**     | Valid numeric price and coordinate formats | Price contained symbols and required numeric transformation |
| **Completeness** | Presence of missing prices                 | Missing values existed and required handling                |
| **Consistency**  | Price formatting (`$120`, `"120"`, etc.)   | Inconsistent syntax required standardization                |
| **Timeliness**   | Dataset represents a single snapshot       | Acceptable because research uses cross-sectional analysis   |

---

## **2. Cleaning Decisions**

Based on profiling, the following cleaning steps were selected:

### **Step 1: Select Only Necessary Columns**

To support integration and analysis, only essential fields were kept:

* `id`
* `latitude`
* `longitude`
* `price`

This avoids carrying unnecessary metadata into downstream files.

---

### **Step 2: Clean Price Formatting**

Raw price values appeared as strings with symbols:

```
"$110", "$82.00", "$215"
```

Cleaning applied:

```python
airbnb['price'] = airbnb['price'].replace('[\$,]', '', regex=True).astype(float)
```

This ensures:

* prices are valid numeric floats
* consistent format for grouping and averaging

---

### **Step 3: Remove Rows with Missing Price**

Listings without price information cannot contribute to the price-related portion of our research question.
Thus, rows missing price were removed:

```python
airbnb = airbnb.dropna(subset=['price'])
```

This improves completeness for the fields needed in aggregation.

---

## **3. Summary of Cleaning Operations (OpenRefine-Style Log)**

The following JSON describes the sequence of transformations in the pipeline (optional for documentation):

```json
[
  {"op": "core/column-removal", "columnName": "listing_url"},
  {"op": "core/column-reorder", "columnNames": ["id", "latitude", "longitude", "price"]},
  {"op": "core/text-transform", "columnName": "price", "expression": "value.replace(\"$\",\"\")"},
  {"op": "core/text-transform", "columnName": "price", "expression": "value.toNumber()"},
  {"op": "core/row-removal", "description": "Remove rows with blank price"}
]
```

This corresponds directly to the Python workflow in `data_cleaning.py`.

---

## **4. Cleaning Script Reference**

```python
import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/airbnb_listings-los-angeles_2025-09-01.csv.gz")
OUT_DIR = Path("data/processed")
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_PATH = OUT_DIR / "airbnb_clean.csv.gz"

airbnb = pd.read_csv(RAW_PATH, compression="gzip", low_memory=False)

airbnb = airbnb[['id', 'latitude', 'longitude', 'price']]
airbnb['price'] = airbnb['price'].replace('[\$,]', '', regex=True).astype(float)
airbnb = airbnb.dropna(subset=['price'])

airbnb.to_csv(OUT_PATH, index=False, compression="gzip")
print(f"Saved cleaned Airbnb data to: {OUT_PATH}")
```

---

## **5. Output**

The cleaned dataset contains:

* numeric prices
* valid coordinates
* only necessary columns
* no missing values in fields required for aggregation

What emerges is a clean, analysis-ready dataset suitable for spatial joining and merging with Zillow values.

---
