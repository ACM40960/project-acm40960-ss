import pandas as pd
from pathlib import Path

# Paths
DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "raw" / "EI-Stats-Review-ALL-data.xlsx"
OUTPUT_PATH = Path(__file__).resolve().parent.parent / "data" / "processed" / "ei_statistical_review" /"ei_co2_emissions.csv"
SHEET_NAME = "CO2 from Energy"

# Load Excel sheet
df = pd.read_excel(DATA_PATH, sheet_name=SHEET_NAME, skiprows=2)

# Drop empty columns and rows
df = df.dropna(how="all").dropna(axis=1, how="all")

# Rename first column to "country"
df.columns.values[0] = "country"

# Drop any footer rows (e.g., world total repeated, notes)
df = df[~df["country"].str.lower().str.contains("source|total", na=False)]

# Melt the dataframe: from wide to long format
df_long = df.melt(id_vars="country", var_name="year", value_name="co2_emissions_mt")

# Convert year to numeric and drop invalid rows
df_long["year"] = pd.to_numeric(df_long["year"], errors="coerce")
df_long = df_long.dropna(subset=["year", "co2_emissions_mt"])

# Convert year to integer and CO2 to float
df_long["year"] = df_long["year"].astype(int)
df_long["co2_emissions_mt"] = pd.to_numeric(df_long["co2_emissions_mt"], errors="coerce")

# Drop rows with missing emissions
df_long = df_long.dropna(subset=["co2_emissions_mt"])

# Optional: sort the data
df_long = df_long.sort_values(["country", "year"])

# Save to CSV
df_long.to_csv(OUTPUT_PATH, index=False)

print(f"CO2 emissions data saved to {OUTPUT_PATH}")
