# Airbnb and Housing Prices Project

Team Members: Jiya Chachan (chachan2), Hannah Adachi (hannaha7)

Link to Output Box Folder: [https://uofi.box.com/s/ae0qoc1qxapa724kxkn94evo6ewjo4zn](https://uofi.box.com/s/ae0qoc1qxapa724kxkn94evo6ewjo4zn)

## Summary

## Data Profile

## Data Quality

## Findings

## Future Work
Throughout this project, we learned several lessons regarding the challenges and realities of working with real-world data. One of the most important lessons was the recognition that a good chunk of data science work occurs long before the actual modeling or analysis steps. A lot of our time was spent acquiring, cleaning, integrating, and validating the data. Preparing the datasets to be structurally compatible for integration and analytically meaningful required more effort than we expected, especially because each source had different formats, levels of granularity, and assumptions. This really reinforced the idea that good analysis depends on the quality of the underlying data. Another major lesson was the importance of reproducibility and documentation. The process of building out our pipeline revealed how easy it is to lose track of those smaller, seemingly insignificant steps and implicit decisions we made along the way. Using workflow tools introduced in class (i.e., Snakemake, OpenRefine) for our project, we learned how valuable explicitly writing out our processes is for the sake of transparency and future reproducibility.

Looking ahead, there are several potential areas for extending and improving the project. One such area involves moving beyond analyzing exclusively based on ZIP codes as the geographic unit. ZIP codes vary widely in size and population, which can hide meaningful data within neighborhoods. Future work could utilize Census tracts to allow for more precise spatial analysis and would likely reveal a more nuanced relationship between the two variables.

Future analysis could also explore more advanced modeling techniques such as spatial regression, geographically weighted regression, or clustering models which could reveal patterns that linear models might miss. Spatial autocorrelation tests, for example, could help determine whether Airbnb activity in one area influences nearby ZIP codes.

Another natural extension of this project would be to expand the analysis to additional cities or states across the United States. Los Angeles is a unique housing market with unusually high home values, tourism activity, and regulatory dynamics, so examining multiple cities would allow us to evaluate whether the patterns we observed generalize beyond our initial analysis. Cities such as New York, San Francisco, Austin, or Miami could serve as meaningful comparison points. Conducting a cross-city or multi-state analysis would also enable us to study how regional factors such as local regulations or tourism economies shape the relationship between short-term rentals and housing prices.

Time-series analysis offers another valuable extension. Both Zillow and Inside Airbnb provide historical data, making it possible to evaluate how the relationship between Airbnb activity and housing values changes over time. Instead of analyzing a single year, future work could identify whether rising Airbnb density precedes increases in home values or simply reflects existing market conditions. This would allow for more robust interpretations and could help clarify the temporal dynamics of short-term rentals within housing markets.

If we wanted to go beyond Airbnb as the single input variable, we could also consider incorporating other factors such as median income, vacancy rates, or population changes to create a multivariable model. Additional datasets from the American Community Survey or local planning agencies could be integrated to explore whether Airbnb remains a significant predictor after controlling for these factors.

## Reproducing

The full detailed reproducibility and workflow automation instructions are located here:
```bash
Reproducibility/README.md
```

**Reproducibility**

To ensure full reproducibility, we provide a clear set of manual steps describing how to reproduce the analysis from start to finish using the individual scripts in our project.

1. Cloning the project repository
Download the full project codebase, including the data acquisition, cleaning, and integration scripts from GitHub repository.

2. Set up the software environment.
Users must create a Python environment and install all required packages listed in requirements.txt to replicate the computational environment used in our project.

3. Download all datasets programmatically.
The project includes scripts that automatically download the InsideAirbnb listings, Zillow ZHVI dataset, and U.S. Census ZCTA shapefiles. No manual downloading is required.

4. (Optional) Verify data integrity.
A checksum script is provided for users who wish to verify the SHA-256 fingerprints of the downloaded datasets.

5. Run the data cleaning script.
This step standardizes formats, filters invalid rows, and prepares Airbnb and Zillow data for integration.

6. Run the data integration script.
This script merges the cleaned datasets with Census ZCTA boundaries, performs spatial joins, computes ZIP-level aggregates, and creates the final integrated dataset used for analysis.

7. Access the final outputs.
After the above steps, users can view the integrated dataset, generated visualizations, and regression results in the designated output folders.
Access results in Box.
All final outputs are also stored in a shared Box folder for convenient review.

Following these steps allows any user to manually reproduce the results exactly as presented in the project.

**Workflow Automation and Provenance**

In addition to the manual reproducibility pathway, our project includes a fully automated workflow implemented using Snakemake. This workflow eliminates the need to run individual scripts and ensures that all results are generated in a controlled, dependency-aware sequence. 


The automated workflow performs the following actions:
* Downloads all required datasets
* Computes optional checksums
* Cleans and preprocesses Airbnb and Zillow data
* Integrates all datasets into a unified ZIP-level file
* Conducts statistical analysis
* Produces final visualizations and summary outputs
Users may execute the entire pipeline with a single command using Snakemake or by running the provided run_all.sh script, which activates the environment and launches the workflow automatically. Snakemake manages all dependencies, ensures proper execution order, and guarantees that each output is traceable back to its inputs.

This automated option serves as a complete alternative to the manual reproducibility steps and provides a transparent record of the data lineage and transformations applied throughout the project.

## References
**Datasets**

Inside Airbnb. (2025). Inside Airbnb: Explore the data–Los Angeles listings. Retrieved from
   https://insideairbnb.com/los-angeles/.

Zillow. (2025). Zillow Home Value Index (ZHVI), ZIP Code Level. Zillow Research. Retrieved
   from https://www.zillow.com/research/data/.

U.S. Census Bureau. (2023). TIGER/Line Shapefiles: ZIP Code Tabulation Areas (ZCTAs). U.S.
   Department of Commerce. Retrieved from
   https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html.

**Software/Tools**

Köster, J. & Rahmann, S. (2012). Snakemake—a scalable bioinformatics workflow engine.
   Bioinformatics, 28(19), 2520–2522.

OpenRefine. (2022). OpenRefine (Version 3.7) [Software]. OpenRefine Project.
   https://openrefine.org/. 
