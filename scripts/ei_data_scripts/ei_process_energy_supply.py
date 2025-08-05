import pandas as pd
from pathlib import Path

# -----------------------------------------------------
# File paths
# -----------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[2]

EI_FILE   = BASE_DIR / "data" / "raw" / "EI-Stats-Review-ALL-data.xlsx"
POP_FILE  = BASE_DIR / "data" / "raw" / "population-long-run-with-projections.csv"
GDP_FILE  = BASE_DIR / "data" / "raw" / "mpd2023_web.xlsx"

OUTPUT_PATH = BASE_DIR / "data" / "processed" / "ei_energy_supply_owid_units.csv"

# -----------------------------------------------------
# Load Primary Energy Consumption (EJ)
# -----------------------------------------------------
df_energy = pd.read_excel(EI_FILE, sheet_name="Primary Energy Cons (old meth)", skiprows=2)
df_energy.columns.values[0] = "country"
df_energy = df_energy.dropna(subset=["country"])
df_energy = df_energy.melt(id_vars=["country"], var_name="year", value_name="primary_energy_consumption_ej")
df_energy["year"] = df_energy["year"].astype(str).str.extract(r"(\d{4})").astype(int)

# -----------------------------------------------------
# Load Population
# -----------------------------------------------------
df_pop = pd.read_csv(POP_FILE)
df_pop = df_pop.rename(columns={"Entity": "country", "Year": "year", "Population (historical)": "population"})
df_pop = df_pop[["country", "year", "population"]]

# -----------------------------------------------------
# Load GDP per capita (in 2011 USD)
# -----------------------------------------------------
df_gdp = pd.read_excel(GDP_FILE, sheet_name="Full data")
df_gdp = df_gdp[df_gdp["year"] >= 1960]
df_gdp = df_gdp.rename(columns={"country": "country", "gdppc": "gdp_per_capita_2011usd"})
df_gdp = df_gdp[["country", "year", "gdp_per_capita_2011usd"]]

# -----------------------------------------------------
# Merge all data
# -----------------------------------------------------
df = pd.merge(df_energy, df_pop, on=["country", "year"], how="inner")
df = pd.merge(df, df_gdp, on=["country", "year"], how="inner")

# -----------------------------------------------------
# Convert and Derive Indicators
# -----------------------------------------------------
EJ_TO_KWH = 2.77777777778e11  # 1 EJ = 2.78 × 10^11 kWh
KWH_TO_TWH = 1e-9

# Total energy consumption in TWh
df["primary_energy_consumption_kwh"] = df["primary_energy_consumption_ej"] * EJ_TO_KWH
df["primary_energy_consumption_twh"] = df["primary_energy_consumption_kwh"] * KWH_TO_TWH

# Derive population and GDP-based metrics
df["energy_per_capita_kwh"] = df["primary_energy_consumption_kwh"] / df["population"]
df["gdp"] = df["gdp_per_capita_2011usd"] * df["population"]
df["energy_per_gdp_kwh"] = df["primary_energy_consumption_kwh"] / df["gdp"]

# -----------------------------------------------------
# Final selection
# -----------------------------------------------------
df = df[[
    "country", "year",
    "primary_energy_consumption_twh",
    "energy_per_capita_kwh",
    "energy_per_gdp_kwh"
]]

# -----------------------------------------------------
# Save
# -----------------------------------------------------
df.to_csv(OUTPUT_PATH, index=False)
print(f"Saved: {OUTPUT_PATH}")
