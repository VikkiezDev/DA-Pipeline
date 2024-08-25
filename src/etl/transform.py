import pandas as pd
import json

# Path to the JSON file
json_file_path = '/home/vignesh-nadar/Desktop/sixtyDays/sprint1/project1/data/temp.json'
csv_file_path = '/home/vignesh-nadar/Desktop/sixtyDays/sprint1/project1/data/raw_data/data.csv'

# Load JSON data from file
with open(json_file_path, 'r') as file:
    json_data = json.load(file)

# Check if 'data' key exists and is a list
if 'data' in json_data and isinstance(json_data['data'], list):
    # Normalize and flatten JSON data
    df = pd.json_normalize(json_data['data'], sep='_')
    
    # Save DataFrame to CSV
    df.to_csv(csv_file_path, index=False)
    print(f"JSON data has been converted to CSV and saved as '{csv_file_path}'.")
else:
    print("Invalid JSON format or 'data' key missing.")

# Process CSV file

print(df)

print(df.columns)