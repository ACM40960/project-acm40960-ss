# GLOBAL HEAT & POLAR RETREAT: TRACKING EMISSIONS, TEMPERATURES, AND ARCTIC CHANGE

## Overview

This project investigates the relationship between atmospheric CO₂ concentrations, global temperature rise, and Arctic sea ice decline. Using over 270 years of historical data, advanced statistical analysis, and machine learning forecasting models, the study aims to quantify human impact on the climate and project future Arctic ice conditions.

The analysis covers:

* Long-term trends in CO₂ emissions and global temperatures.
* Statistical correlation and causality analysis.
* Forecasting of Arctic sea ice extent, area, and thickness.
* Scenario-based projections for an “ice-free” Arctic.

---

## Motivation

The Arctic serves as a climate amplifier — warming faster than much of the globe and influencing global weather patterns. Rising CO₂ levels from fossil fuel use, industrial processes, and deforestation are driving temperature increases and accelerating ice loss.
Understanding these patterns is critical for anticipating environmental, economic, and geopolitical consequences, and for shaping informed climate policy.

---

## Project Structure

```
project-acm40960-ss/
│
├── data/
│   ├── final/
│   │   ├── final_arctic.csv
│   │   ├── whole_data_merged.csv
│   ├── pre_processed/
│   │   ├── arctic_sia_sie_monthly.csv
│   │   ├── co2&energy_merged.csv
│   │   ├── ei_energy_supply.csv
│   │   ├── era5_arctic_merged_clean.csv
│   │   ├── global_temp_data.csv
│   │   └── ...
│   └── raw/
│       ├── Fossil CO2 emissions.csv
│       ├── Global_TAVG_annual.txt
│       ├── National_Fossil_Carbon_Emissions_...
│       └── ...
│
├── scripts/
│   ├── analysis_and_modelling/
│   │   ├── arctic_vs_global_temp.ipynb
│   │   ├── co2_analysis.ipynb
│   │   ├── co2vstemp&energy_world.ipynb
│   │   ├── final_arctic_analysis.ipynb
│   │   ├── global_correlation.ipynb
│   │   ├── models.ipynb
│   │   └── temp_analysis.ipynb
│   └── pre_processing/
│       ├── arctic_area_extent.ipynb
│       ├── arctic_final_merge.ipynb
│       ├── arctic_predictors.ipynb
│       ├── arctic_thickness.ipynb
│       ├── co2_source.ipynb
│       ├── ei_process_energy_supply.ipynb
│       ├── global_temp.ipynb
│       └── whole_data_merge.ipynb
│
├── README.md
└── ...
```

---

## Data Sources

* **Temperature:** HadCRUT, NOAA, IPCC datasets.
* **CO₂ Concentrations:** Mauna Loa Observatory, ice core reconstructions, Global Carbon Budget datasets.
* **Arctic Sea Ice:** Copernicus Climate Data Store, NSIDC satellite observations (extent, area, thickness).
* **Energy & Emissions:** IEA, National and global fossil fuel datasets.

---

## Methodology

1. **Data Preprocessing**

   * Merging multiple climate datasets (temperature, CO₂, energy, sea ice).
   * Cleaning and interpolating missing values.
   * Converting raw formats into structured CSVs for analysis.

2. **Exploratory Analysis**

   * Trend analysis of CO₂, global temperature, and Arctic sea ice.
   * Statistical correlation and regression modeling.
   * Seasonal and annual breakdowns.

3. **Modelling & Forecasting**

   * Regression models for CO₂–temperature relationships.
   * Time-series models (ARIMA, Holt’s trend, SARIMAX).
   * Machine learning models (SVR, LSTM) for Arctic ice forecasting.
   * Projection of “ice-free” Arctic thresholds (<1 million km²).

---

## Expected Outcomes

* Quantitative validation of CO₂–temperature correlation.
* Informative visualizations with uncertainty bands and trend lines.
* Forecasts estimating the year of seasonal Arctic ice-free conditions.
* Data-driven insights to inform climate change mitigation policies.

---

## Installation & Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/ACM40960/project-acm40960-ss.git
   cd project-acm40960-ss
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Open Jupyter notebooks in the `scripts/` directory for analysis and modeling.

---

## References

1. Intergovernmental Panel on Climate Change (IPCC). (2021). *Climate Change 2021: The Physical Science Basis*.
2. Jarvis, A., & Forster, P. M. (2024). *Estimated human-induced warming...*, *Nature Geoscience*.
3. Su, Z. (2022). *World CO₂ Emissions...*, *Highlights in Science, Engineering and Technology*.
4. Zaatar, T., et al. (2025). *Arctic sea ice thickness prediction using ML*, *Annals of Operations Research*.

---new changes!
