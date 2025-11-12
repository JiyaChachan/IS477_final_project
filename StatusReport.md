# Status Report

## Updated Tasks
**Weeks 1-2 (Early October 2025)**
* Set up the project and confirm dataset licensing and ethics compliance.
During the initial two weeks, our team focused on establishing the foundation of the project and confirming that both datasets complied with ethical and legal data-use requirements. We reviewed the documentation and licensing information for both the Inside Airbnb and Zillow Home Value Index datasets. We confirmed that the Inside Airbnb data are distributed under the Creative Commons Attribution 4.0 International License (CC By 4.0) which allows for reuse and modification with proper attribution. For Zillow, we verified the dataset's Terms of Use, ensuring that our project complied with their requirements to cite "Data provided by Zillow Group" on all visualizations and derived works. After realizing the Inside Airbnb data did not include ZIP codes to easily merge the two datasets, we added a third dataset from the US Census Bureau. This dataset is public domain created by the federal government, meaning it can be downloaded, shared, and used without restriction. The US Census Bureau requests attribution when data are cited or used in publications. We also created the GitHub repository and organized our project files to ensure a reproducible workflow and clear file structure.

**Week 3 (Mid-October)**
* Data collection and acquisition
In week 3, we collected the Inside Airbnb and Zillow data and performed the initial cleaning process. The Airbnb and Zillow datasets were loaded and the Census shapefile is read using geopandas. The Airbnb data was cleaned by dropping unnecessary columns, handling missing values, and ensuring coordinates were numeric. The Zillow data was standardized by renaming key columns, selecting relevant fields, and ensuring consistent ZIP code formatting. The Census shapefile was simplified to include only geographic boundaries and ZCTA identifiers. The Airbnb data’s latitude and longitude values were converted into geographic points and spatially joined to the Census shapefile to assign each listing a corresponding ZIP code. We then performed checks to confirm ZIP codes were accurately aligned and then output summary statistics to verify successful integration. We made sure to include clear code comments to easily trace the data pipeline from raw files to merged dataset.

**Weeks 4-5 (Late October)**
* Data storage and organization
We organized the repository into distinct folders for data collection and acquisition. Each file was named using standardized conventions to ensure traceability. We also created metadata files that describe each dataset's schema, source URL, license type, and data dictionary references. A README was added to the GitHub repository outlining the overall data workflow and citing both sources appropriately. We verified that all files were properly stored, backed up, and versioned on GitHub. This organization ensures that future collaborators or instructors can easily reproduce our work.

**Week 6 (Late October - Early November)**
* Data extraction, enrichment, and integration
We developed Python scripts using pandas to merge the Airbnb and Zillow datasets on ZIP code, creating a unified dataset for analysis. We handled schema differences by normalizing column formats (e.g., converting string ZIP codes to integers and aligning date fields). We also applied appropriate cleaning methods to the merged dataset such as imputing missing median prices, verifying ZIP code integrity, and ensuring that temporal fields aligned across both datasets. All scripts were committed to the GitHub repository with descriptive commit messages and included in the project’s documentation folder. The merged dataset was exported in CSV format for flexible downstream analysis.

**Week 7 (Early November)**
* Set up workflow automation using Jupyter notebooks and scripts for reproducibility.
During week 7, our team focused on improving workflow automation and reproducibility. We integrated our Python scripts into Jupyter notebooks, allowing the entire data process – from acquisition to integration – to be executed and documented in a single, reproducible environment. All code and outputs were organized within the GitHub repository to ensure transparency and version control. We also completed and submitted the Interim Status Report, summarizing our progress through Week 7 and outlining our next steps.

---

## Updated Timeline
**Weeks 8–10 (Mid to Late November):**
Focus on reproducibility and transparency.
* Jiya finalizes scripts and creates the data dictionary.
* Hannah documents dependencies and makes sure all files are clearly labeled and explained.

**Week 11 (December):**
Prepare Final Project Submission (due December 10, 2025).
* Hannah writes the analysis and findings section.
* Jiya finalizes visualizations and formatting.
* Both review the whole project together to make sure everything is complete, consistent, and ready for submission on GitHub.

---

## Changes to Project Plan
We made a key adjustment to our project plan after discovering that the Inside Airbnb dataset did not include ZIP code information, making smooth integration with the Zillow dataset difficult. To resolve this, we incorporated a third dataset from the U.S. Census Bureau’s TIGER/Line shapefiles, which provide geographic boundary data, including ZIP Code Tabulation Areas (ZCTAs). This dataset allowed us to geocode Airbnb listings and map them to corresponding ZIP codes, enabling accurate spatial alignment with the Zillow data. The addition of the Census dataset slightly expanded our project scope to include geospatial preprocessing, but it also strengthened the overall data integrity and integration process. We updated our project documentation and metadata to reflect this change and ensured that the new dataset was properly cited and stored in accordance with licensing and ethical requirements.

Another change that we made to our project plan was in response to instructor feedback regarding our lack of specificity for our dataset’s data use licenses. Initially our plan mentioned verifying dataset licenses but did not specify the exact terms or attribution requirements. After review, we expanded this section to clearly document these requirements (as described in ‘Updated Tasks: Weeks 1-2’ above). The newly added U.S. Census Bureau data were also reviewed and confirmed to be public domain, as they are U.S. government data. These revisions ensure our project fully aligns with ethical and legal data use standards while improving transparency and compliance documentation.

---

## Team Member Contributions
**Jiya**

**Hannah**
My contributions to this project focused on ensuring compliance with data licensing requirements and documentation. I reviewed and documented the licensing terms for the three datasets, confirming that we were following all requirements regarding Terms of Use and the CC Attribution 4.0 License. I also formatted and updated our interim status report with our weekly progress, dataset integration milestones, and updates to the project plan.
