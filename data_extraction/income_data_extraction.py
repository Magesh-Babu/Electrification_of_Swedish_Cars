import requests
import json
import pandas as pd

# --- Step 1: Define constants ---
url = "https://api.scb.se/OV0104/v1/doris/en/ssd/START/AA/AA0003/AA0003F/IntGr5Kom"

# --- Step 2: Create reusable function ---
def fetch_income_data():
    query = {
        "query": [
            {
                "code": "Bakgrund",
                "selection": {
                    "filter": "vs:IntegrationBakgrundÅlder",
                    "values": [
                            "tot20-64",
                            "20-24",
                            "25-34",
                            "35-44",
                            "45-54",
                            "55-64"
                        ]
                    }
                },
            {
                "code": "ContentsCode",
                 "selection": {
                    "filter": "item",
                    "values": [
                            "AA0003GI"
                    ]
                }
            }
        ],
        "response": {
            "format": "json-stat2"
        }
    }

    response = requests.post(url, json=query)
    
    if response.status_code != 200:
        print(f"⚠️ Failed for income data extraction — Status Code: {response.status_code}")
        return pd.DataFrame()  # Return empty DataFrame to skip

    data = response.json()

    # Extract dimensions
    regions = data['dimension']['Region']['category']['label']
    variable = data['dimension']['Bakgrund']['category']['label']
    year = data['dimension']['Tid']['category']['label']

    variable_codes = list(variable.keys())
    region_codes = list(regions.keys())
    year_codes = list(year.keys())
    values = data['value']

    records = []
    index = 0
    for region_code in region_codes:
        for variable_code in variable_codes:
            for year_code in year_codes:    
                records.append({
                    "Region": regions[region_code],
                    "AgeVariable": variable_code,
                    "Year": year[year_code],
                    "AvgDisposibleIncome": values[index]
                })
                index += 1

    return pd.DataFrame(records)

# --- Step 3: Fetch and save data ---
income_df = fetch_income_data()
income_df.to_csv("income_statistics.csv", index=False)
print("✅ All income data saved to income_statistics.csv")

# Optional: Show summary
print(income_df.head())
