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
This project will use two datasets:

1. **Inside Airbnb Dataset** – [https://insideairbnb.com/get-the-data/](https://insideairbnb.com/get-the-data/)  
   Provides data on Airbnb listings for various cities, including location, price, and availability.

2. **Zillow Home Value Index (ZHVI)** – [https://www.zillow.com/research/data/](https://www.zillow.com/research/data/)  
   Contains information on housing prices and rental values by ZIP code across the United States.

These two datasets will be integrated using location data (ZIP code or neighborhood) to explore the relationship between Airbnb activity and housing prices.

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
One key constraint in this project is the availability and timeliness of the data. Both the Inside Airbnb and Zillow datasets are publicly accessible but may not always include the most recent updates, limiting our ability to analyze real-time trends or make the most accurate conclusions. Additionally, since the data is secondhand (collected and published by third parties other than our team), we have to assume they followed the proper data handling, collection, and storage practices. Another challenge lies in the data integration step. The two datasets could contain inconsistent labeling (e.g., city boundary lines) or missing values, making it harder to compare the two sources. These differences may affect the precision of our analysis when relating Airbnb activity to housing prices. Finally, given the large size of these datasets, computational efficiency and data cleaning may be additional constraints we will face when developing and testing our workflow.

---

## Gaps
At this stage of the semester, our project plan and knowledge base is limited by the topics we have covered so far in the course. As a result, several areas of our proposed workflow and timeline will need additional input and refinement as we learn the remaining modules. For instance, we have not yet covered Data Integration, which will be essential for combining the Airbnb and Zillow datasets by ZIP code or neighborhood. We also have limited knowledge of other topics such as Workflow Automation and Provenance, Reproducibility and Transparency, and Metadata and Data Documentation, which are all critical for building a fully automated and reproducible end-to-end pipeline. These are areas we will be looking to revisit and expand upon in detail once those topics are covered.
