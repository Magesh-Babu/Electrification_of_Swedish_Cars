import pandas as pd
import re

def load_raw_data(filepath: str) -> pd.DataFrame:
    return pd.read_csv(filepath)

def extract_coordinates(df: pd.DataFrame) -> pd.DataFrame:
    df['wgs84'] = df['Geometry'].apply(eval).apply(lambda x: x.get('WGS84', None))
    df[['longitude', 'latitude']] = df['wgs84'].str.extract(r'POINT \(([-\d.]+) ([-\d.]+)\)')
    df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
    df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
    return df.drop(columns=['wgs84'])

def standardize_timestamps(df: pd.DataFrame, time_col: str = "MeasurementTime") -> pd.DataFrame:
    df[time_col] = pd.to_datetime(df[time_col], errors='coerce')
    return df

def validate_data(df: pd.DataFrame) -> pd.DataFrame:
    null_summary = df.isnull().sum()
    print("\nNull values summary:\n", null_summary)
    return df.dropna()

def clean_data(filepath: str, output_path: str):
    df = load_raw_data(filepath)
    df = extract_coordinates(df)
    df = standardize_timestamps(df)
    df = validate_data(df)
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    clean_data("raw_traffic_data.csv", "cleaned_traffic_data.csv")
