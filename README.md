# Airbnb and Housing Prices Project

Team Members: Jiya Chachan (chachan2), Hannah Adachi (hannaha7)

## Reproducibility Instructions
### Step 1: Clone the repository
To download the project, run the following code in your terminal:
```bash
git clone https://github.com/JiyaChachan/IS477_final_project.git
cd IS477_final_project
```

### Step 2: Setting up the environment
We recommend using a virtual environment to avoid dependency issues. This will install all required packages (pandas, geopandas, matplotlib, etc.).
```bash
python3 -m venv venv
source venv/bin/activate      # Windows → venv\Scripts\activate
pip install -r requirements.txt
```

### Step 3: Download all datasets
```bash
python "Data collection and acquisition/download_airbnb_data.py"
python "Data collection and acquisition/download_zillow_data.py"
python "Data collection and acquisition/download_census_zcta_data.py"
```
The project includes a helper script checksum.py that computes SHA-256 checksums for the downloaded datasets. To verify file integrity manually, run:
```bash
python "Data collection and acquisition/checksum.py"
```

### Step 4: Run data cleaning
```bash
python "Data Cleaning/data_cleaning.py"
```

### Step 5: Run data integration 
This step will merge the cleaned datasets by ZIP/ZCTA.
```bash
python "Data Integration/data_integration.py"
```

### Step 6: Run data analysis & visualization
....
