import pandas as pd
from pathlib import Path

# Set input and output paths
DATA_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "raw" / "EI-Stats-Review-ALL-data.xlsx"
OUTPUT_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "processed" / "ei_statistical_review" / "ei_total_co2eq_emissions.csv"
SHEET_NAME = "CO2e Emissions "

# Load the sheet (skiprows=2 to remove metadata/header rows)
df = pd.read_excel(DATA_PATH, sheet_name=SHEET_NAME, skiprows=2)

# Drop empty columns and rows
df = df.dropna(how="all").dropna(axis=1, how="all")

# Rename first column to "country"
df.rename(columns={df.columns[0]: "country"}, inplace=True)

# Melt the DataFrame to long format
df_melted = df.melt(id_vars=["country"], var_name="year", value_name="total_co2eq_emissions_mt")
df_melted["year"] = pd.to_numeric(df_melted["year"], errors="coerce")
df_melted = df_melted.dropna(subset=["year"]).astype({"year": int})

# Drop rows with missing emission values
df_melted = df_melted.dropna(subset=["total_co2eq_emissions_mt"])

# Save to CSV
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
df_melted.to_csv(OUTPUT_PATH, index=False)

print(f"Processed and saved: {OUTPUT_PATH}")
