# Reproducibility and Transparency
## Reproducibility Instructions
### Step 1: Clone the repository

```sh
git clone https://github.com/JiyaChachan/IS477_final_project.git
cd IS477_final_project
```

### Step 2: Setting up the environment
We recommend using a virtual environment to avoid dependency issues. This will install all required packages (pandas, geopandas, matplotlib, etc.).
```sh
python3 -m venv venv
source venv/bin/activate      # Windows → venv\Scripts\activate
pip install -r requirements.txt
```

### Step 3: Download all datasets programmatically
```bash
python "Data collection and acquisition/download_airbnb_data.py"
python "Data collection and acquisition/download_zillow_data.py"
python "Data collection and acquisition/download_census_zcta_data.py"
```
These scripts download:
* Airbnb listings (Los Angeles)
* Zillow ZHVI ZIP-level home value data
* U.S. Census ZCTA shapefiles
No datasets need to be downloaded manually.

### Step 4: Verify integrity with checksums
```bash
python "Data collection and acquisition/checksum.py"
```
This prints SHA-256 checksums for each raw dataset so users may confirm file integrity. This step is optional and not required to run the workflow.

### Step 5: Run data cleaning
```bash
python "Data Quality & Cleaning/data_cleaning.py"
```
This script standardizes data types, filters invalid records, reformats ZIP codes, and outputs cleaned Airbnb and Zillow datasets.

### Step 6: Run data integration
```bash
python "Data Integration/data_integration.py"
```
This step spatially joins Airbnb listings to Census ZCTAs, merges the resulting ZIP-level aggregates with Zillow home values, produces visualizations, and outputs the final integrated dataset:
```bash
data/processed/merged_airbnb_zillow_by_zip.csv
```
### Step 7: Run Data analysis and visualization
```bash
python "Data Analysis/analysis_visualization.py"
```
This step will fit the OLS regression model, generate the scatterplot, and create summary analysis outputs. You can also find our output findings in the Box folder [here](https://uofi.box.com/s/ae0qoc1qxapa724kxkn94evo6ewjo4zn) or all outputs are stored in predictable locations:

```
visualizations/airbnb_vs_homevalues.png
```

```
analysis/ols_summaries.txt
```

## Automated Workflow
This project is fully reproducible through the automated Snakemake workflow located in:
```nginx
Workflow automation and provenance/Snakefile
```
All results including data downloads, data cleaning, integration, statistical analysis, and visualizations can be regenerated from scratch by following the steps below:
### Step 1: Clone the repository

```sh
git clone https://github.com/JiyaChachan/IS477_final_project.git
cd IS477_final_project
```

### Step 2: Setting up the environment
We recommend using a virtual environment to avoid dependency issues. This will install all required packages (pandas, geopandas, matplotlib, etc.).
```sh
python3 -m venv venv
source venv/bin/activate      # Windows → venv\Scripts\activate
pip install -r requirements.txt
```

### Step 7: Verify required directory structure

Snakemake will populate the following directories automatically:

```
data/raw/
data/processed/
visualizations/
analysis/
```

### Step 8: Run the full workflow

From the repository root:

```sh
snakemake -s "Workflow automation and provenance/Snakefile" --cores 1
```

Snakemake will:

1. Download Airbnb listings
2. Download Zillow home value data
3. Download Census ZCTA shapes
4. Optionally compute checksums
5. Clean the Airbnb dataset
6. Merge Airbnb, Zillow, and ZCTA datasets
7. Run statistical analysis
8. Generate a visualization

### Step 9: Final outputs

After the workflow completes, key artifacts appear in:

* `data/processed/merged_airbnb_zillow_by_zip.csv`
* `visualizations/airbnb_vs_homevalues.png`
* `analysis/ols_summaries.txt`

These are the final deliverables of the automated pipeline.

---

## Run All script

This script allows a user to re execute the entire workflow with a single command and without remembering the Snakemake options.

`run_all.sh`:

```sh
#!/bin/bash
set -e

cd "$(dirname "$0")/.."

echo "Activating environment..."
source venv/bin/activate || conda activate is477

echo "Running Snakemake workflow..."
snakemake -s "Workflow automation and provenance/Snakefile" --cores 1

echo "Workflow complete."
```

Make it executable:

```sh
chmod +x "Workflow automation and provenance/run_all.sh"
```

Now users can run:

```sh
./"Workflow automation and provenance"/run_all.sh
```

## Outputs Produced Automatically
After the workflow completes, the following reproducible artifacts will be generated:
```bash
data/processed/merged_airbnb_zillow_by_zip.csv
visualizations/airbnb_vs_homevalues.png
analysis/ols_summaries.txt
```
These are the final deliverables used in our analysis.

## Transparency
### Data Access
All datasets used in the workflow were retrieved programmatically, meaning:
* No manual data downloads are required
* Running the workflow will always fetch the most recent version of each dataset

### Software and License
* All software dependencies are specified in `requirements.txt`
* Workflow scripts, automation files, and analysis scripts are included in the repository
* Dataset licenses are documented in the licensing section located in this file:
```nginx
Metadata and Documentation/README.md
```
