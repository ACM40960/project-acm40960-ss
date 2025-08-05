import xarray as xr
import numpy as np
import pandas as pd
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parents[1]

# Load the existing energy + global temp dataset
input_path = BASE_DIR / "data" / "processed" / "ei_energy_emissions_with_global_temp.csv"
df_merged = pd.read_csv(input_path)

# Load Arctic gridded temperature NetCDF file
arctic_path = BASE_DIR / "data" / "raw" / "Global_TAVG_Gridded_0p25deg.nc"
ds = xr.open_dataset(arctic_path)

# Extract temperature, latitude, time
temperature = ds["temperature"]
latitudes = ds["latitude"]
times = ds["time"]

# Step 1: Filter for Arctic region (latitude >= 66.5°N)
arctic_temp = temperature.sel(latitude=latitudes[latitudes >= 66.5])

# Step 2: Extract year from time
years = pd.to_datetime(times.values).year
arctic_temp["year"] = ("time", years)

# Step 3: Compute annual mean Arctic anomaly
arctic_df = (
    arctic_temp
    .groupby("year")
    .mean(dim=["latitude", "longitude"], skipna=True)
    .to_dataframe()
    .reset_index()[["year", "temperature"]]
    .rename(columns={"temperature": "arctic_anomaly_c"})
)

# Step 4: Merge with existing dataset
df_final = pd.merge(df_merged, arctic_df, on="year", how="left")

# Step 5: Save to processed folder
output_path = BASE_DIR / "data" / "processed" / "ei_energy_emissions_with_global_and_arctic_temp.csv"
df_final.to_csv(output_path, index=False)

print("✅ Final merged shape:", df_final.shape)
print(df_final[["country", "year", "global_temp_c", "arctic_anomaly_c"]].drop_duplicates().head())
