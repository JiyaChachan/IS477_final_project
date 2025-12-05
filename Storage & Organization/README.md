# **Storage and Organization**

This repository follows a modular, lifecycle-based structure that mirrors the major phases of data work: acquisition, cleaning, integration, analysis, documentation, reproducibility, and workflow automation. Each stage is self-contained, with scripts, documentation, and outputs grouped together. This organization supports clarity, traceability, and full reproducibility.

---

# **Repository Structure**

```
/
├── Data collection and acquisition/
│   ├── checksum.py
│   ├── download_airbnb_data.py
│   ├── download_census_zcta_data.py
│   ├── download_zillow_data.py
│   └── README.md
│
├── Data Quality & Cleaning/
│   ├── data_cleaning.py
│   ├── history.json
│   └── README.md
│
├── Data Integration/
│   ├── data_integration.py
│   └── README.md
│
├── Data Analysis/
│   ├── analysis_visualization.py
│   ├── results.txt
│   ├── airbnb_vs_homevalues.png
│   └── README.md
│
├── Metadata and Documentation/
│   └── README.md
│
├── Reproducibility/
│   ├── environment.txt
│   └── README.md
│
├── Storage & Organization/
│   └── README.md
│
├── Workflow automation and provenance/
│   ├── Snakefile
│   ├── run_all.sh
│   └── README.md
│
├── ProjectPlan.md
├── StatusReport.md
├── requirements.txt
└── README.md
```

---

# **Directory Purpose and Naming Conventions**

## **1. Data collection and acquisition/**

This module contains all scripts that retrieve external datasets used in the project.

**Contents include:**

* `download_airbnb_data.py`
* `download_zillow_data.py`
* `download_census_zcta_data.py`
* `checksum.py` for SHA-256 dataset validation
* A README explaining source URLs, provenance, and licensing

**Conventions:**

* Acquisition scripts follow the pattern `download_<source>_data.py`
* No downloaded data is stored in GitHub
  The scripts write to `data/raw/` when executed locally.

---

## **2. Data Quality & Cleaning/**

This directory contains scripts that profile and clean raw datasets before integration.

**Contents include:**

* `data_cleaning.py` for processing, filtering, and standardizing data
* `history.json` documenting cleaning operations
* README describing quality checks, profiling, and assumptions

**Outputs generated (not versioned):**

* Cleaned datasets in `data/processed/`

**Conventions:**

* Cleaning scripts use `data_<task>.py`
* Provenance logs use JSON (`history.json`)

---

## **3. Data Integration/**

This stage merges datasets into a unified analytical file.

**Contents include:**

* `data_integration.py` performing spatial joins, ZIP aggregation, and merging Zillow values
* README describing integration logic and schema alignment

**Generated output:**

* `merged_airbnb_zillow_by_zip.csv` stored in `data/processed/`

**Conventions:**

* Integration code always named `data_integration.py`
* Outputs stored in processed data folder, not the script directory

---

## **4. Data Analysis/**

This module contains analytical scripts, visualizations, and derived results.

**Contents include:**

* `analysis_visualization.py`
* `airbnb_vs_homevalues.png`
* `results.txt`
* README summarizing the analysis methods

**Conventions:**

* Analysis scripts follow `analysis_<task>.py`
* Visualizations are lowercase descriptive filenames
  Example: `airbnb_vs_homevalues.png`
* Textual output stored as `results.txt`

This ensures results are reproducible from the workflow and are separate from raw or intermediate data.

---

## **5. Metadata and Documentation/**

Central location for project metadata, data dictionaries, and descriptive documentation.

**Contents include:**

* `README.md` explaining schema, variables, and metadata standards

**Conventions:**

* Documentation uses TitleCase
* Contains no code and no generated outputs

---

## **6. Reproducibility/**

This folder ensures others can recreate your exact environment.

**Contents include:**

* `environment.txt` describing package dependencies
* `README.md` with instructions for environment recreation

**Conventions:**

* Only reproducibility files here
* No data or workflow code

---

## **7. Storage & Organization/**

This directory documents how datasets, scripts, and outputs should be structured.

**Contents include:**

* `README.md` describing organizational conventions and storage standards

This folder is documentation only.

---

## **8. Workflow automation and provenance/**

This module contains your full workflow automation system using Snakemake.

**Contents include:**

* `Snakefile` defining all workflow rules for acquisition, cleaning, integration, and analysis
* `run_all.sh` script to execute the entire pipeline
* README explaining workflow dependencies and usage

**Conventions:**

* Workflow file always named `Snakefile`
* Shell automation scripts use snake_case suffix `.sh`
* Provenance descriptions stored in README

---

## **9. Top-Level Files**

| File               | Purpose                                       |
| ------------------ | --------------------------------------------- |
| `README.md`        | Full project overview, metadata, instructions |
| `requirements.txt` | Python dependencies for running the pipeline  |
| `ProjectPlan.md`   | Initial planning document                     |
| `StatusReport.md`  | Progress tracking and updates                 |

---

# **Naming and Storage Conventions Summary**

| Category            | Convention                  | Example                       |
| ------------------- | --------------------------- | ----------------------------- |
| Acquisition scripts | `download_<source>_data.py` | `download_zillow_data.py`     |
| Cleaning scripts    | `data_cleaning.py`          | ✓                             |
| Integration scripts | `data_integration.py`       | ✓                             |
| Analysis scripts    | `analysis_<task>.py`        | `analysis_visualization.py`   |
| Visualizations      | lowercase descriptive       | `airbnb_vs_homevalues.png`    |
| Provenance          | lowercase                   | `checksum.py`, `history.json` |
| Reports             | TitleCase                   | `ProjectPlan.md`              |

