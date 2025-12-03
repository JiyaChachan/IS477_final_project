#!/usr/bin/env python3
"""
analysis_visualization.py

Performs exploratory analysis and visualization on the merged Airbnb-Zillow dataset.

"""

import os
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Paths
MERGED_CSV = Path("data/processed/merged_airbnb_zillow_by_zip.csv")
VIS_DIR = Path("visualizations")
ANALYSIS_DIR = Path("analysis")
VIS_DIR.mkdir(parents=True, exist_ok=True)
ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)

OUT_PLOT = VIS_DIR / "airbnb_vs_homevalues.png"
OUT_SUMMARY = ANALYSIS_DIR / "ols_summaries.txt"

# Load merged data
if not MERGED_CSV.exists():
    raise FileNotFoundError(f"Merged dataset not found: {MERGED_CSV}. Run data_integration.py first.")
merged = pd.read_csv(MERGED_CSV)

# Ensure numeric columns are numeric
merged['num_listings'] = pd.to_numeric(merged['num_listings'], errors='coerce')
merged['median_home_value'] = pd.to_numeric(merged['median_home_value'], errors='coerce')

# Drop rows with missing values in analysis columns
merged = merged.dropna(subset=['num_listings', 'median_home_value']).reset_index(drop=True)

# 1) Correlation (overall)
corr_overall = merged[['num_listings', 'median_home_value']].corr().iloc[0,1]
print(f"Overall correlation between num_listings and median_home_value: {corr_overall:.4f}")

# 2) Scatter plot
plt.figure(figsize=(8,6))
plt.scatter(merged['num_listings'], merged['median_home_value'], alpha=0.6)
plt.xlabel('Number of Airbnb Listings per ZIP Code')
plt.ylabel('Median Home Value ($)')
plt.title('Airbnb Density vs. Home Values (Los Angeles)')
plt.grid(True)
plt.tight_layout()
plt.savefig(OUT_PLOT, dpi=300)
plt.close()
print(f"Saved scatterplot to: {OUT_PLOT}")

# 3) Simple OLS: median_home_value ~ num_listings
X_simple = sm.add_constant(merged['num_listings'])
y = merged['median_home_value']
model_simple = sm.OLS(y, X_simple).fit()
print("Simple OLS summary (median_home_value ~ num_listings):")
print(model_simple.summary())

# 4) Neighborhood classification (if not present)
if 'neighborhood_type' not in merged.columns:
    merged['neighborhood_type'] = np.where(
        merged['num_listings'] > merged['num_listings'].median(),
        'Urban Core',
        'Suburban'
    )

# 5) Group means
group_means = merged.groupby('neighborhood_type')['median_home_value'].mean()
print("\nMean median_home_value by neighborhood_type:")
print(group_means.to_string())

# 6) Per-group correlation
per_group_corrs = {}
for group in merged['neighborhood_type'].unique():
    subset = merged[merged['neighborhood_type'] == group]
    if len(subset) >= 2:
        corr = subset[['num_listings', 'median_home_value']].corr().iloc[0,1]
    else:
        corr = np.nan
    per_group_corrs[group] = corr
    print(f"{group}: correlation = {corr:.4f}")

# 7) Interaction model: median_home_value ~ num_listings + is_urban + num_listings:is_urban
merged['is_urban'] = (merged['neighborhood_type'] == 'Urban Core').astype(int)
X = merged[['num_listings', 'is_urban']].copy()
X = sm.add_constant(X)
X['interaction'] = X['num_listings'] * X['is_urban']
y = merged['median_home_value']
model_inter = sm.OLS(y, X).fit()
print("\nInteraction OLS summary (with is_urban and interaction):")
print(model_inter.summary())

# 8) Save textual summaries and stats
with open(OUT_SUMMARY, "w") as f:
    f.write("Overall correlation (num_listings vs median_home_value):\n")
    f.write(f"{corr_overall:.6f}\n\n")
    f.write("Simple OLS: median_home_value ~ num_listings\n")
    f.write(model_simple.summary().as_text())
    f.write("\n\nGroup mean median_home_value by neighborhood_type:\n")
    f.write(group_means.to_string())
    f.write("\n\nPer-group correlations:\n")
    for k, v in per_group_corrs.items():
        f.write(f"{k}: {v}\n")
    f.write("\n\nInteraction OLS: median_home_value ~ num_listings + is_urban + interaction\n")
    f.write(model_inter.summary().as_text())

print(f"Saved OLS summaries and group stats to: {OUT_SUMMARY}")
