import pandas as pd
from pathlib import Path

# Set input and output paths
DATA_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "raw" / "EI-Stats-Review-ALL-data.xlsx"
OUTPUT_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "processed" / "ei_statistical_review" / "ei_carbon_prices.csv"

SHEET_NAME = "Carbon Prices"

# Load the sheet
df = pd.read_excel(DATA_PATH, sheet_name=SHEET_NAME, skiprows=2)

# Drop empty columns and rows
df = df.dropna(how="all").dropna(axis=1, how="all")

# Rename first column
df.rename(columns={df.columns[0]: "region"}, inplace=True)

# Melt to long format
df_melted = df.melt(id_vars=["region"], var_name="year", value_name="carbon_price_usd_per_tco2")
df_melted["year"] = pd.to_numeric(df_melted["year"], errors="coerce")
df_melted = df_melted.dropna(subset=["year"]).astype({"year": int})

# Drop rows with missing carbon prices
df_melted = df_melted.dropna(subset=["carbon_price_usd_per_tco2"])

# Save to CSV
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
df_melted.to_csv(OUTPUT_PATH, index=False)

print(f"Processed and saved: {OUTPUT_PATH}")
