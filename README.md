# Airbnb and Housing Prices Project

Team Members: Jiya Chachan (chachan2), Hannah Adachi (hannaha7)

Link to Output Box Folder: [https://uofi.box.com/s/ae0qoc1qxapa724kxkn94evo6ewjo4zn](url)
## Licenses for Data and Software/Code
Our project uses three external datasets. Their licenses are:
### InsideAirbnb Data
* Source: [http://insideairbnb.com](url)
* License: Inside Airbnb Terms of Use
* Permissions: Data is available for non-commercial, academic use.

### Zillow ZHVI Data
* Source: Zillow Research Data Portal
* License: Zillow Data Usage Terms (non-commercial use)
* Permissions: May be used for research and academic purposes; redistribution is restricted.

### U.S. Census TIGER/Line Shapefiles (ZCTA)
* Source: U.S. Census Bureau
* License: Public Domain (U.S. Government work)
* Permissions: Free to use, copy, modify, and redistribute.

### Software/Code License
All software created by our group for this IS 477 project is released under the following license:

**MIT License**: Our code is released under the MIT License, which allows reuse for academic and non-commercial purposes.


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
```bash
python "Data Analysis/analysis_visualization.py"
```

