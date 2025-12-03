# **Data Analysis and Visualization Documentation**

This document describes the procedures used to analyze the integrated Airbnb–Zillow dataset and generate visualizations. All analysis steps were executed using the script:

```
analysis_visualization.py
```

The analysis uses the merged ZIP-level dataset produced earlier:

---

## **1. Load Analysis Dataset**

The merged dataset includes, for each ZIP code:

* number of Airbnb listings (`num_listings`)
* average Airbnb price
* median Zillow home value (`median_home_value`)
* neighborhood classification (`Urban Core` or `Suburban`)

Before analysis, the script:

* loads the dataset,
* ensures numeric fields are numeric,
* drops rows with missing values in the analysis columns.

---

## **2. Correlation Analysis**

To measure the strength of linear association between Airbnb density and housing prices, the Pearson correlation coefficient was calculated:

```python
merged[['num_listings', 'median_home_value']].corr()
```

This produces the overall correlation between:

* **number of Airbnb listings per ZIP**, and
* **median home value in that ZIP**.

The result is printed and included in the final ols_summaries summary.

---

## **3. Visualization: Scatterplot**

A scatterplot was generated to visualize the relationship between Airbnb density and home values:

```python
plt.scatter(merged['num_listings'], merged['median_home_value'], alpha=0.6)
```

The figure includes:

* x-axis: number of Airbnb listings
* y-axis: median home value
* title and labels for interpretability

The plot is saved to:

```
airbnb_vs_homevalues.png
```

This visualization helps determine whether a positive or negative trend is visible.

---

## **4. Simple Linear Regression (OLS)**

To quantify the relationship, an Ordinary Least Squares (OLS) regression was fit:

```python
X = sm.add_constant(merged['num_listings'])
y = merged['median_home_value']
model = sm.OLS(y, X).fit()
```

Model form:

```
median_home_value = β0 + β1 * num_listings
```

The script prints the full regression summary, including:

* coefficient estimates
* t-statistics and p-values
* R-squared value
* confidence intervals

This output is saved to:

```
ols_summaries.txt
```

---

## **5. Group Comparison: Urban Core vs Suburban**

To explore whether the relationship differs by neighborhood type, ZIP codes were grouped using the existing classification:

* **Urban Core** = listing count above median
* **Suburban** = listing count below median

The script computes:

* mean home values per group
* pairwise correlations within each group

```python
merged.groupby('neighborhood_type')['median_home_value'].mean()
```

```python
subset[['num_listings', 'median_home_value']].corr()
```

These statistics help interpret whether the relationship varies by neighborhood category.

---

## **6. Interaction Regression Model**

To formally test whether the relationship between Airbnb density and home values differs between Urban Core and Suburban ZIPs, an interaction model was fitted:

```python
merged['is_urban'] = (merged['neighborhood_type'] == 'Urban Core').astype(int)
X['interaction'] = X['num_listings'] * X['is_urban']
model_inter = sm.OLS(y, X).fit()
```

Model form:

```
median_home_value = β0 + β1*num_listings + β2*is_urban + β3*(num_listings × is_urban)
```

This shows:

* whether Urban Core ZIPs systematically differ in home values
* whether the slope between listings and home values differs by neighborhood type

The full summary is also saved to:

```
ols_summaries.txt
```

---

## **7. Final Output Storage**

All outputs are stored in predictable locations:

### **Figures**

```
airbnb_vs_homevalues.png
```

### **Text-Based ols_summaries**

```
ols_summaries.txt
```
