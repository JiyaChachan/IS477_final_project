# Airbnb and Housing Prices Project

Team Members: Jiya Chachan (chachan2), Hannah Adachi (hannaha7)

Link to Output Box Folder: [https://uofi.box.com/s/ae0qoc1qxapa724kxkn94evo6ewjo4zn](https://uofi.box.com/s/ae0qoc1qxapa724kxkn94evo6ewjo4zn)

## Summary
This project investigates the relationship between short-term Airbnb rental activity and local housing prices by designing and implementing an end-to-end, fully reproducible data workflow. The main research question guiding our work is whether the density of Airbnb activity is associated with increases in local home values, and whether this relationship varies across different types of neighborhoods, such as dense urban areas compared to more suburban regions. This topic has become increasingly relevant as cities across the United States debate the role of short-term rentals in influencing housing affordability, neighborhood structures, and real estate investment patterns. Los Angeles, a city with both a large tourism market and persistent affordability challenges, provides the ideal context for examining how Airbnb activity aligns with housing price trends.

Public debate often suggests that Airbnb activity may reduce the availability of long-term housing. At the same time, others argue that Airbnb simply reflects the underlying market conditions rather than driving them. These opposing ideas are what motivated us to explore whether measurable patterns exist between the two. Our project doesn’t aim to determine causality, but rather to document whether a statistical relationship is observable at the ZIP-code level. 

To address this question, we integrated three distinct datasets: Inside Airbnb listings for Los Angeles, Zillow’s Home Value Index (ZHVI), and U.S. Census Bureau ZIP Code Tabulation Area (ZCTA) shapefiles. One obstacle emerged early in which we discovered that the Inside Airbnb dataset does not contain ZIP codes. We needed these ZIP codes in order to compare Inside Airbnb’s records with Zillow’s housing prices. To resolve this problem, we incorporated the third dataset (Census shapefiles) and performed a spatial join to assign each listing to a ZIP code based on its latitude and longitude coordinates. This step highlights how important schema-level alignment and record-level integration are in facilitating a comparable analysis and measurable findings.
	
Once the data was integrated and cleaned, we conducted exploratory and statistical analysis to identify whether any broad patterns existed. At a high level, our results indicate a modest positive association between Airbnb listing density and median home values across Los Angeles ZIP codes. Visual exploration shows that neighborhoods with unusually high Airbnb activity often fall within higher-priced areas of Los Angeles, which aligns with broader expectations about how short-term rentals cluster in already desirable markets. Statistical analysis supports this overall trend, though the effect is modest and does not explain most of the variation in housing prices across the city. When comparing urban and suburban neighborhoods, we observed that urban areas are typically more expensive and have more Airbnb activity, but the underlying relationship between Airbnb presence and housing costs appears relatively similar across both contexts. Taken together, the findings suggest that Airbnb is associated with higher housing prices, but it is likely only one of many factors influencing affordability in Los Angeles.
	
Overall, this project demonstrates how data curation and integration practices enable meaningful analysis of complex, real-world questions. By applying the principles of the data lifecycle (acquisition, cleaning, integration, analysis, and documentation), we were able to create a reproducible workflow that transforms three heterogeneous datasets into a singular structure able to reveal potential housing trends. Our findings should not be interpreted as causal, but they do reveal important spatial patterns and provide a foundation for future research.

## Data Profile
This project relies on three publicly available datasets that together allow for a structured analysis of short term rental activity and housing market conditions across ZIP Code Tabulation Areas (ZCTAs). The datasets come from Inside Airbnb, the Zillow Home Value Index (ZHVI), and the U.S. Census Bureau’s TIGER/Line ZCTA shapefiles. Each dataset provides a different type of information and is governed by different permissions or licensing rules, which must be respected throughout the project. Understanding the content of these datasets and their ethical or legal constraints is central to ensuring that the analysis is both valid and responsible.

The Inside Airbnb dataset is the first major component of this project. Inside Airbnb is an independent initiative that compiles information scraped from Airbnb’s public website. It publishes these datasets under the Creative Commons Attribution 4.0 International license (CC BY 4.0), which allows sharing, reuse, and modification as long as proper credit is given to the original creator. The dataset includes detailed listing information such as host identifiers, listing IDs, geographic coordinates, rental prices, availability, property characteristics, and neighborhood names. These details make it possible to understand the distribution and characteristics of Airbnb listings across a city. However, even though the data is legally available for reuse, it still contains potentially sensitive elements, such as exact coordinates of private residences and identifiers for hosts. Because there is a possibility of indirect identification, this project avoids presenting results at the individual listing level. All analysis and outputs aggregate Airbnb records to the ZIP code level, which reduces privacy risks while still allowing meaningful insights based on the broader patterns in the dataset. Proper attribution is also provided in accordance with the CC BY 4.0 license.

The second dataset is the Zillow Home Value Index, a product of Zillow’s housing market research program. ZHVI provides an estimate of typical home values across different geographic areas, including ZIP codes, and reflects the middle price point of homes in a given region. This dataset is made available through Zillow’s research portal, but it is not licensed under an open license like Creative Commons. Instead, Zillow permits the use of its data for academic, non commercial purposes under its Terms of Use. These terms also restrict redistribution of the raw dataset, meaning that while the project may use ZHVI for analysis, it cannot publish or share the dataset itself. Only aggregated or derived results, such as summary statistics or visualizations, appear in the final report. Although ZHVI is based on aggregated housing market estimates rather than individual property records, the legal constraints on redistribution must be followed carefully to comply with Zillow’s use policy.

The third dataset used in the project is the U.S. Census Bureau’s TIGER/Line ZCTA shapefiles. These files define the geographic boundaries of ZIP Code Tabulation Areas, which are approximations of postal ZIP codes used for statistical and mapping purposes. Unlike the other datasets, the Census shapefiles are fully in the public domain under United States law, since they are produced by a federal agency. This means they are free to use, modify, and redistribute without any restrictions. The shapefiles include geographic polygon boundaries, GEOID identifiers, and spatial metadata that allow Airbnb listings to be assigned to the correct ZCTA based on their coordinates. This step is essential because the Inside Airbnb dataset does not include ZIP codes directly. By linking Airbnb listings to ZCTAs, the project can align short term rental information with ZIP code level housing value estimates from ZHVI. The Census shapefiles contain no personal or sensitive information, so there are no ethical concerns associated with their use.

Bringing these datasets together requires attention not only to their technical compatibility but also to their ethical and legal constraints. Inside Airbnb’s CC BY 4.0 license requires proper attribution and encourages privacy aware use of listing level data, which this project follows by working only with aggregated values. Zillow’s Terms of Use limit the sharing of raw ZHVI data, which the project respects by including only summary results in the analysis. The Census shapefiles pose no limitations, but they serve a crucial role in ensuring that Airbnb listings are assigned to consistent geographic areas. By adhering to each dataset’s licensing rules and ethical guidelines, the project maintains responsible data practices while creating a reliable foundation for the subsequent analytical steps.

## Data Quality
Evaluating and improving data quality was an essential part of preparing this project’s datasets for integration and analysis. Because the workflow combines Inside Airbnb listings, Zillow Home Value Index (ZHVI) data, and U.S. Census ZCTA shapefiles, the assessment had to address both the quality of each individual dataset and the quality of the merged dataset. This section summarizes the key quality findings using the four major dimensions of data quality: accuracy, completeness, consistency, and timeliness.

The first dataset assessed was the Inside Airbnb listings. Accuracy was most affected by the formatting of the price variable. Prices appeared with dollar signs, commas, or inconsistent string formats, which prevented them from being treated as numeric values. This issue required cleaning to ensure that price values reflected accurate numerical amounts. Geographic coordinates, however, were generally accurate and fell within expected ranges for Los Angeles. Completeness posed another challenge. A small portion of listings were missing price values, which meant they could not contribute to ZIP code level averages. These rows were removed because missing prices would lead to inaccurate or biased aggregation. Consistency problems also appeared, primarily in how prices were formatted differently across listings. Selecting only the relevant columns and standardizing price formatting helped resolve these issues. In terms of timeliness, the Airbnb dataset represents a single snapshot of listings from a specific date. Because the project uses cross-sectional analysis, this snapshot was considered timely and appropriate for the research goals.

The Zillow Home Value Index dataset underwent a similar quality assessment, though its issues were different in nature. In terms of accuracy, Zillow’s home value estimates are aggregated and model derived, so no cleaning of numeric values was needed. Completeness was generally strong for the selected time period, although some ZIP codes had missing values in earlier months. Because the project focused on a single recent month of ZHVI, this did not create problems. Zillow’s biggest quality issue involved consistency. ZIP codes were stored as integers without leading zeros, which caused mismatches when merging with datasets that stored ZIP codes as five digit strings. Standardizing ZIP codes by padding them with zeros ensured that different files aligned correctly. Regarding timeliness, Zillow updates its datasets monthly, and the version used in this project reflects recent housing conditions, making it suitable for analysis.

The U.S. Census ZCTA shapefiles introduced yet another set of quality considerations. Accuracy depended on properly aligning coordinate reference systems (CRS). The shapefiles used the NAD83 coordinate system, while the Airbnb data used WGS84 (EPSG:4326). Without correcting this mismatch, spatial joins would produce inaccurate or invalid ZIP code assignments. Reprojecting the shapefiles ensured accurate alignment. Completeness of ZCTA boundaries was not an issue because Census shapefiles provide full geographic coverage. Consistency across shapefile attributes was also strong, as the Census Bureau maintains standardized metadata and spatial structure. As for timeliness, Census shapefiles represent geographic boundaries for a specific year. They do not update frequently, but ZIP boundaries also do not change dramatically year to year, so this did not pose a problem.

The final set of quality assessments focused on integration across datasets. Accuracy was most important during the spatial join between Airbnb listings and ZCTAs. Even after aligning coordinate systems, a small number of Airbnb points fell outside any ZCTA polygon. These listings were excluded to avoid inaccurate ZIP code assignments. Completeness issues emerged when merging Airbnb and Zillow data because some ZIP codes existed in one dataset but not the other. Using an inner join ensured that each row in the final dataset contained complete information for listings, prices, and housing values. Consistency checks focused on ensuring that all ZIP codes across datasets shared the same format and that aggregated statistics matched expected patterns. Duplicate ZIP codes, mismatched boundaries, and formatting inconsistencies were addressed before the final merge. In terms of timeliness, the integration combined datasets from the same general time period: Airbnb listings from a given date, ZHVI from the same year, and ZCTA boundaries from the most recent Census release. This alignment helped avoid mixing outdated geographic or housing value data with current listing information.

Overall, the data quality assessment revealed several issues but also confirmed that each dataset could be prepared for reliable integration. Cleaning Airbnb data improved accuracy and consistency, standardizing Zillow ZIP codes resolved compatibility issues, and verifying the CRS of ZCTA boundaries enabled accurate spatial joins. Integration level checks ensured that ZIP code matches were valid and that the final merged dataset contained complete, consistent, and timely information. These steps ultimately strengthened the quality of the dataset used in the analysis and provided a solid foundation for deriving meaningful insights.



## Findings
The analysis explored whether ZIP codes with a higher density of Airbnb listings tend to experience higher housing costs, and whether this pattern varies across different types of neighborhoods. The scatterplot comparing Airbnb density and median home values shows a loose but noticeable upward trend. Many ZIP codes in Los Angeles cluster at the lower end of the distribution, with fewer than 200 Airbnb listings and home values generally below one million dollars. However, ZIP codes with very high Airbnb activity, particularly those above 600 or 1000 listings, tend to fall into higher home value ranges. This pattern visually suggests that areas with more Airbnb listings also tend to be more expensive housing markets.

This visual impression is supported, though modestly, by the statistical results. The overall correlation between the number of Airbnb listings and median home values is about 0.245, indicating a weak but positive relationship . While this is not a strong association, it does imply that ZIP codes with more Airbnb activity generally have higher housing costs. The simple OLS model strengthens this interpretation. In the regression predicting median home value from listing density, the model estimates that each additional Airbnb listing is associated with an increase of about 570 dollars in the median home value. This effect is statistically significant but small, and the model explains only around six percent of the variation in home values across ZIP codes. These findings suggest that Airbnb density alone cannot account for most neighborhood price differences but does have a measurable association with them.

To address the question of whether this relationship differs across neighborhood types, ZIP codes were divided into Urban Core and Suburban categories based on Airbnb density. Here, the differences were more pronounced in overall housing levels than in the strength of the correlation. Urban Core ZIP codes had much higher average home values, around 1.17 million dollars, compared to about 955 thousand dollars in Suburban ZIP codes. This shows that areas with heavy Airbnb activity are generally more expensive neighborhoods to begin with. When correlations were calculated separately for each group, the Suburban category showed almost no relationship between Airbnb presence and home value, while the Urban Core category showed a slightly stronger positive correlation of around 0.21 . This suggests the Airbnb housing price relationship is more pronounced in dense, urban neighborhoods where both housing demand and short-term rental activity tend to be higher.

To test whether Airbnb density affects neighborhoods differently depending on their classification, an interaction regression model was estimated. This model compared the influence of listing density in Urban Core versus Suburban ZIP codes. Although the model explained slightly more variance, none of the interaction terms were statistically significant. This result indicates that while Urban Core ZIP codes differ strongly in levels of Airbnb activity and overall home values, the effect of adding more listings does not differ meaningfully between urban and suburban areas. In other words, Airbnb density is associated with higher housing costs, but this association is relatively consistent across neighborhood types once baseline price differences are accounted for.

Bringing these findings together, the analysis provides partial support for the idea that Airbnb activity relates to local housing prices. ZIP codes with more listings tend to have higher median home values, and this relationship is most evident in denser urban neighborhoods. However, the effect is modest and explains only a small portion of the variation in the housing market. The results suggest that Airbnb may play a contributing role in higher housing costs, but it is likely one factor among many broader economic and neighborhood characteristics shaping affordability in Los Angeles.


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
