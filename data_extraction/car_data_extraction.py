import requests
import json
import pandas as pd

# --- Step 1: Define constants ---
url = "https://api.scb.se/OV0104/v1/doris/en/ssd/START/TK/TK1001/TK1001A/PersBilarDrivMedel"
fuel_codes = ["100", "110", "120", "130", "140", "150", "160", "190"]

# --- Step 2: Create reusable function ---
def fetch_data_for_fuel(fuel_code):
    query = {
        "query": [
            {
                "code": "Drivmedel",
                "selection": {
                    "filter": "item",
                    "values": [fuel_code]
                }
            }
        ],
        "response": {
            "format": "json-stat2"
        }
    }

    response = requests.post(url, json=query)
    
    if response.status_code != 200:
        print(f"⚠️ Failed for fuel code {fuel_code} — Status Code: {response.status_code}")
        return pd.DataFrame()  # Return empty DataFrame to skip

    data = response.json()

    # Extract dimensions
    regions = data['dimension']['Region']['category']['label']
    fuels = data['dimension']['Drivmedel']['category']['label']
    months = data['dimension']['Tid']['category']['label']

    fuel_label = list(fuels.values())[0]
    region_codes = list(regions.keys())
    month_codes = list(months.keys())
    values = data['value']

    records = []
    index = 0
    for region_code in region_codes:
        for month_code in month_codes:
            records.append({
                "Region": regions[region_code],
                "FuelType": fuel_label,
                "YearMonth": months[month_code],
                "NumberOfRegistration": values[index]
            })
            index += 1

    return pd.DataFrame(records)

# --- Step 3: Loop through fuel codes and collect data ---
all_dataframes = []

for code in fuel_codes:
    print(f"Fetching for fuel code: {code}")
    df_part = fetch_data_for_fuel(code)
    if not df_part.empty:
        all_dataframes.append(df_part)

# --- Step 4: Combine and save ---
final_df = pd.concat(all_dataframes, ignore_index=True)
final_df.to_csv("csv_files/car_registration.csv", index=False)
print("✅ All data saved to car_registration.csv")

# Optional: Show summary
print(final_df['FuelType'].value_counts())
print(final_df.head())
