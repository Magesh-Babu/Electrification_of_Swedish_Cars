import requests
import os
import json
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("TRAFIKVERKET_API_KEY")

TRAFFICFLOW_FIELDS = [
    "AverageVehicleSpeed",
    "VehicleFlowRate",
    "MeasurementTime",
    "Geometry",
    "VehicleType",
    "CountyNo",
    "RegionId"
]

def build_xml_query():
    fields_xml = "".join([f"<INCLUDE>{field}</INCLUDE>" for field in TRAFFICFLOW_FIELDS])
    return f"""
    <REQUEST>
      <LOGIN authenticationkey=\"{API_KEY}\"/>
      <QUERY objecttype=\"TrafficFlow\" namespace=\"Road.TrafficInfo\" schemaversion=\"1.5\">
        {fields_xml}
      </QUERY>
    </REQUEST>
    """

def fetch_traffic_flow():
    url = "https://api.trafikinfo.trafikverket.se/v2/data.json"
    xml_query = build_xml_query()

    response = requests.post(url, data=xml_query.encode('utf-8'), headers={"Content-Type": "text/xml"})

    if response.status_code == 200:
        data = response.json()
        traffic_data = data['RESPONSE']['RESULT'][0]['TrafficFlow']
        return pd.DataFrame(traffic_data)
    else:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")

def save_to_csv(df: pd.DataFrame, filename: str):
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    df_raw = fetch_traffic_flow()
    save_to_csv(df_raw, "raw_traffic_data.csv")
