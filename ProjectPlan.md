# Project Plan

## Overview
The goal of this project is to design and implement a comprehensive end-to-end data workflow that utilizes the principles of data curation, integration, and reproducible analysis we have learned throughout this course. The project will focus on addressing a real-world question with an analysis of two distinct data sources. By applying the data lifecycle concepts, the project aims to reach meaningful conclusions while maintaining ethical data management practices.

---

## Research Question(s)
The main question this project aims to address is **how the density of Airbnb listings within a neighborhood or ZIP code relates to local housing prices or rental rates.**  

Specifically, we want to explore whether areas with a higher number of Airbnb listings tend to have higher housing costs, suggesting that short-term rentals might be influencing housing affordability.  

We are also interested in whether this relationship varies across different types of neighborhoods (e.g., urban vs. suburban areas) and if the effect changes over time as Airbnb activity increases.  

Overall, the goal is to understand if there is a measurable connection between the growth of Airbnb and the rising cost of housing, using publicly available data from **Inside Airbnb** and **Zillow**.

---

## Team
This project will be completed collaboratively by **Jiya** and **Hannah**, with both team members contributing equally throughout the entire data lifecycle.  

- **Hannah** will focus on reviewing the datasets, checking data licenses, and organizing the project files and folders in GitHub. She will also take the lead on maintaining documentation and writing parts of the reports.  
- **Jiya** will focus on the technical aspects of the project, including acquiring and processing the data, writing Python scripts for cleaning and integration, and creating visualizations for analysis.

Both Jiya and Hannah will work together on writing and editing the **Project Plan**, **Interim Status Report**, and **Final Report**. They plan to meet regularly to discuss progress, divide tasks, and make decisions together. By clearly sharing responsibilities and keeping open communication, they will ensure all parts of the project are consistent, reproducible, and completed on time.

---

## Datasets
This project will use two main datasets: Inside Airbnb and Zillow Home Value Index (ZHVI). These datasets work well together because one focuses on short-term rentals (Airbnb) and the other on long-term housing prices (Zillow). By combining them, we can study how the number of Airbnb listings in an area might relate to housing costs.

**1. Inside Airbnb Dataset**    
**Source:** [https://insideairbnb.com/get-the-data/](https://insideairbnb.com/get-the-data/)  
**Permissions:** Data compiled by Murray Cox. Licensed under [CC By 4.0](url).

The Inside Airbnb dataset gives detailed information about Airbnb listings in many cities around the world. It collects data from Airbnb’s public website and is updated regularly throughout the year. Each city’s dataset includes information such as:  
- The **listing ID** and **host information** (for example, how many listings one host has)  
- The **location** (latitude, longitude, neighborhood, and ZIP code)  
- **Property details** (room type, number of bedrooms, price per night)  
- **Availability and reviews** (how often the place is available, number of reviews, etc.)  

For this project, we will focus on one large city and group listings by **ZIP code or neighborhood**. This will let us measure how many Airbnb listings are in each area and find the average price and activity level.  


**2. Zillow Home Value Index (ZHVI)**     
**Source:** [https://www.zillow.com/research/data/](https://www.zillow.com/research/data/)  
**Permissions:** Data provided by Zillow Group. Used under Zillow's Terms of Use for non-commercial, academic purposes. No affiliation or endorsement by Zillow Group is implied.

The Zillow Home Value Index (ZHVI) is a large dataset that shows typical home prices across the U.S. It is updated every month and includes data by **ZIP code, city, county, or state**. Zillow calculates these values using many housing records and statistical models.  

Each row in the dataset usually includes:  
- The **location** (ZIP code, city, and state)  
- The **median home value** (the middle price of homes in that area)  
- A **time series** showing how prices have changed over the months or years  

Zillow also provides another dataset called the **Zillow Observed Rent Index (ZORI)**, which shows rental prices. We may use both ZHVI (home prices) and ZORI (rents) to compare Airbnb activity with both housing and rental costs.  


After our data collection and acquisition phase, we realized the Inside Airbnb dataset does not include ZIP codes to easily merge the two datasets. Because of this, we added a third dataset to our project, as described below:

** 3. U.S. Census Bureau TIGER/Line Shapefiles**
**Source:** https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html
**Permissions:** Public domain -- US Government data provided by the U.S. Census Bureau. These files are free to use, modify, and redistribute without restriction under U.S. law (Title 17 U.S.C. §105).

The TIGER/Line shapefiles are geographic boundary datasets that include spatial representations of features such as **ZIP Code Tabulation Areas (ZCTAs)**, census tracts, counties, and other administrative or statistical boundaries across the United States.

Each shapefile includes:
- **Geographic boundaries** defining ZIP Code Tabulation Areas (ZCTAs)
- **FIPS and GEOID codes** identifying each geographic unit
- **Coordinate data** for mapping and spatial joins

For this project, we specifically use the ZCTA shapefiles to assign ZIP codes to Airbnb listings based on their latitude and longitude coordinates. This enables accurate geographic alignment between the Inside Airbnb dataset and the ZHVI dataset. This will allow us to compare areas with lots of Airbnb listings to their average housing prices or rent levels. By analyzing these together, we can see if neighborhoods with more Airbnbs also have higher housing costs or if that pattern changes over time.  

---

## Timeline

**Weeks 1–2 (Early October 2025):**  
Set up the project and confirm dataset licensing and ethics compliance.  
- Hannah reviews dataset documentation and verifies permissions.  
- Jiya sets up the GitHub repository and organizes the project folders.

**Week 3 (Mid-October):**  
Data collection and acquisition.  
- Hannah downloads and cleans the Inside Airbnb dataset.  
- Jiya collects and preprocesses the Zillow Home Value Index data.  
- Both maintain detailed notes on data collection and challenges.

**Weeks 4–5 (Late October):**  
Data storage and organization.  
- Hannah organizes raw and processed data folders.  
- Jiya creates metadata files and initial documentation.
- We’ll make sure everything is stored properly and can be easily reproduced later.  

**Week 6 (Late October – Early November):**  
Data extraction, enrichment, and integration.  
- Jiya writes Python scripts to combine datasets by ZIP code.  
- Hannah checks data quality and handles missing or inconsistent values.

**Week 7 (Early November):**  
Set up workflow automation using Jupyter notebooks and scripts for reproducibility.  
- Prepare **Interim Status Report** (due **November 11, 2025**).  
- Review progress and update plan based on feedback.

**Weeks 8–10 (Mid to Late November):**  
Focus on reproducibility and transparency.  
- Jiya finalizes scripts and creates the data dictionary.  
- Hannah documents dependencies and make sure all files are clearly labeled and explained.

**Week 11 (December):**  
Prepare **Final Project Submission** (due **December 10, 2025**).  
- Hannah writes the analysis and findings section.  
- Jiya finalizes visualizations and formatting.  
- Both review the whole project together to make sure everything is complete, consistent, and ready for submission on GitHub.

---

## Constraints
One key constraint in this project is the availability and timeliness of the data. Both the Inside Airbnb and Zillow datasets are publicly accessible but may not always show the most recent data. Even though Inside Airbnb and Zillow update their data often, there is usually a short delay between when the data is collected and when it becomes available, limiting our ability to analyze real-time trends or make the most accurate conclusions. Additionally, since the data is secondhand (collected and published by third parties other than our team), we have to assume they followed the proper data handling, collection, and storage practices. Another challenge lies in the data integration step. The two datasets could contain inconsistent labeling (e.g., city boundary lines) or missing values, making it harder to compare the two sources. These differences may affect the precision of our analysis when relating Airbnb activity to housing prices. Finally, given the large size of these datasets, computational efficiency and data cleaning may be additional constraints we will face when developing and testing our workflow.

---

## Gaps
At this stage of the semester, our project plan and knowledge base is limited by the topics we have covered so far in the course. As a result, several areas of our proposed workflow and timeline will need additional input and refinement as we learn the remaining modules. For instance, we have not yet covered Data Integration, which will be essential for combining the Airbnb and Zillow datasets by ZIP code or neighborhood. We also have limited knowledge of other topics such as Workflow Automation and Provenance, Reproducibility and Transparency, and Metadata and Data Documentation, which are all critical for building a fully automated and reproducible end-to-end pipeline. These are areas we will be looking to revisit and expand upon in detail once those topics are covered.
