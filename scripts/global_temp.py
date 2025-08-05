import pandas as pd
from pathlib import Path

# Load EI final dataset (already processed)
BASE_DIR = Path(__file__).resolve().parents[1]
ei_path = BASE_DIR / "data" / "processed" / "ei_energy_supply_owid_units.csv"
df_ei = pd.read_csv(ei_path)

# Load global temperature (from previous step)
temp_path = BASE_DIR / "data" / "raw" / "Global_TAVG_annual.txt"
BASELINE_TEMP_C = 14.13

df_temp = pd.read_csv(
    temp_path,
    delim_whitespace=True,
    comment="%",
    header=None,
    names=["year", "anomaly_c", "uncertainty_c", "five_year_avg", "five_year_unc"]
)

# Calculate absolute temperature
########################
# "Absolute temp = Anomaly + 1951–1980 mean (14.13°C)"
########################

df_temp["global_temp_c"] = df_temp["anomaly_c"] + BASELINE_TEMP_C

# Keep only necessary columns
df_temp = df_temp[["year", "anomaly_c", "global_temp_c"]]

# Merge temperature with EI data (retain all EI rows)
df_merged = pd.merge(df_ei, df_temp, on="year", how="left")

# Save the final dataset
output_path = BASE_DIR / "data" / "processed" / "ei_energy_emissions_with_global_temp.csv"
df_merged.to_csv(output_path, index=False)

print("Merged dataset shape:", df_merged.shape)
print(df_merged[["country", "year", "global_temp_c"]].drop_duplicates().head())
