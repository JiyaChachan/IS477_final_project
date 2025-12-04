## Workflow Reproducibility Guide

This project uses Snakemake to automate data acquisition, cleaning, integration, and analysis for the Airbnb–Zillow housing project. The workflow ensures that all intermediate steps run in the correct order and that final outputs can be regenerated at any time with a single command.

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

### Step 3: Verify required directory structure

Snakemake will populate the following directories automatically:

```
data/raw/
data/processed/
visualizations/
analysis/
```

### Step 5: Run the full workflow

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

### Step 6: Final outputs

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
