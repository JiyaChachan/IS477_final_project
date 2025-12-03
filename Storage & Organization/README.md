# **Storage and Organization**

This project is organized into a modular directory structure aligned with the stages of the data lifecycle. Each major phase of the workflow is contained in its own top-level folder, with scripts, intermediate outputs, and documentation stored together. This structure ensures traceability, reproducibility, and clear data provenance.

---

## **Repository Structure**

```
/
├── Data collection and acquisition/
│   ├── README.md
│   ├── checksum.py
│   ├── download_airbnb_data.py
│   ├── download_census_zcta_data.py
│   └── download_zillow_data.py
│
├── Data Quality & Cleaning/
│   ├── README.md
│   ├── data_cleaning.py
│   └── history.json
│
├── Data Integration/
│   ├── README.md
│   └── data_integration.py
│
├── Data Analysis/
│   ├── README.md
│   ├── airbnb_vs_homevalues.png
│   ├── analysis_visualization.py
│   └── results.txt
│
├── Workflow automation and provenance/
│   ├── README.md
│   └── Snakefile
│
│── Workflow automation and provenance/
|── ProjectPlan.md
├── StatusReport.md
├── requirements.txt
└── README.md
```

---

## **Directory Purpose and Naming Conventions**

### **1. Data collection and acquisition/**

This folder contains all scripts used to download datasets directly from external sources (Inside Airbnb, Zillow, and the U.S. Census).

**Naming conventions:**

* Scripts start with `download_` to indicate external acquisition.
* `checksum.py` contains reproducible verification logic.
* Associated dataset README documents URLs, checksums, and attribution.

**Files stored here:** only *scripts* and *documentation*, not raw data.

Raw datasets (Airbnb CSV, Zillow CSV, and ZCTA shapefiles) are downloaded into your local machine under the paths expected by these scripts, but they are intentionally **not committed to GitHub** due to licensing and file size restrictions.

---

### **2. Data Quality & Cleaning/**

This module contains the logic for profiling and cleaning raw datasets.

**Naming conventions:**

* `data_cleaning.py` performs transformations (column selection, price cleaning, NA removal).
* `history.json` records the sequence of transformations in a structured format.

**Outputs:** cleaned files are written to `data/processed/` (not stored in GitHub).

---

### **3. Data Integration/**

This folder includes scripts that perform spatial operations and merge datasets.

**Naming conventions:**

* `data_integration.py` includes the spatial join (Airbnb → ZCTA), ZIP aggregation, Zillow value merge, and classification of neighborhood types.

**Outputs:**
`merged_airbnb_zillow_by_zip.csv` is created in the processed data directory.

---

### **4. Data Analysis/**

This folder contains all analytics code and derived results produced after integration.

**Naming conventions:**

* Scripts use the pattern `analysis_visualization.py`
* Visualization outputs follow descriptive snake_case filenames, e.g.,
  `airbnb_vs_homevalues.png`
* Text-based model results are written to `results.txt`

This separation ensures analysis results can be regenerated via the workflow without mixing them with raw or intermediate data.

---

### **5. Workflow automation and provenance/**

This folder contains:

* Documentation describing workflow reproducibility
* **Snakemake workflow** (`Snakefile`) which automates the entire pipeline from acquisition → cleaning → integration → visualization.

**Naming conventions:**

* High-level reports use TitleCase (`ProjectPlan.md`, `StatusReport.md`)
* Workflow description uses lowercase (`README.md`)
* Pipeline file is always named `Snakefile`

This folder provides traceability and ensures that anyone can regenerate the full project using a single workflow command.

---

### **6. Top-Level Files**

#### **README.md**

Main documentation page, including:

* final report
* reproducibility guide
* metadata
* data dictionary
* licensing
* summary of scripts

#### **requirements.txt**

#### **ProjectPlan.md** and **StatusReport.md**

---

## **Naming and Storage Conventions Summary**

| Category            | Convention                  | Example                       |
| ------------------- | --------------------------- | ----------------------------- |
| Acquisition scripts | `download_<source>_data.py` | `download_airbnb_data.py`     |
| Cleaning scripts    | `data_cleaning.py`          | ✓                             |
| Integration scripts | `data_integration.py`       | ✓                             |
| Analysis scripts    | `analysis_<task>.py`        | `analysis_visualization.py`   |
| Visualizations      | lowercase, descriptive      | `airbnb_vs_homevalues.png`    |
| Reports             | TitleCase                   | `ProjectPlan.md`              |
| Provenance          | lowercase                   | `checksum.py`, `history.json` |

---
