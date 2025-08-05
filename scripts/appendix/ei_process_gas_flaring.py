import pandas as pd
from pathlib import Path

# === File paths ===
DATA_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "raw" / "EI-Stats-Review-ALL-data.xlsx"
OUTPUT_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "processed" / "ei_statistical_review" / "ei_gas_flaring.csv"


# === Sheet name ===
SHEET_NAME = "Natural Gas Flaring"

# === Load the sheet ===
df = pd.read_excel(DATA_PATH, sheet_name=SHEET_NAME, skiprows=2)

# === Clean column names ===
df.columns = df.columns.astype(str).str.strip()

# === Drop empty rows and columns ===
df = df.dropna(how="all").dropna(axis=1, how="all")

# === Rename first column to 'country' ===
if df.columns[0].lower() != "country":
    df = df.rename(columns={df.columns[0]: "country"})

# === Reshape to long format ===
df_long = df.melt(id_vars="country", var_name="year", value_name="gas_flaring_bcm")

# === Extract year and clean values ===
df_long["year"] = df_long["year"].astype(str).str.extract(r"(\d{4})")[0]
df_long = df_long.dropna(subset=["year", "gas_flaring_bcm"])
df_long["year"] = df_long["year"].astype(int)
df_long["gas_flaring_bcm"] = pd.to_numeric(df_long["gas_flaring_bcm"], errors="coerce")

# === Drop rows with missing flaring values ===
df_long = df_long.dropna(subset=["gas_flaring_bcm"]).reset_index(drop=True)

# === Sort for readability ===
df_long = df_long.sort_values(by=["country", "year"])

# === Save to CSV ===
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
df_long.to_csv(OUTPUT_PATH, index=False)

print(f"Natural gas flaring data saved to: {OUTPUT_PATH}")
