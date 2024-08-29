import pandas as pd
import json
import re

# Paths
json_file_path = '/home/vignesh-nadar/Desktop/sixtyDays/sprint1/project1/data/raw_data/raw_data.json'
csv_file_path = '/home/vignesh-nadar/Desktop/sixtyDays/sprint1/project1/data/raw_data/raw_data.csv'
cleaned_data_path = '/home/vignesh-nadar/Desktop/sixtyDays/sprint1/project1/data/processed_data/processed_data.csv'

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

data = pd.read_csv(csv_file_path)
df = data.copy()

df.drop(columns=["id", "url", "referenceId", "posterId", "postDate", "postedTimestamp", "company_id", "company_logo", "company_url", "benefits"], inplace=True)

extracted = df['location'].str.extract(r'(.*?)\((On-site|Remote|Hybrid)\)')

df['location'] = extracted[0].fillna(df['location'])
df['work_place'] = extracted[1]

import re
def extract_state(location):
    # Regular expression to find the state name which is before ', India'
    match = re.search(r'(?<=, )[^,]+(?=, India)', location)
    if match:
        return match.group(0)
    else:
        return None

df['location'] = df['location'].apply(extract_state)

df.loc[42, 'location'] = 'Karnataka'

df['postAt'] = df['postAt'].str.split(' ').str[0]

df.drop(columns=['title'], inplace=True)

to_str = ['location', 'type', 'company_name', 'work_place']
df[to_str] = df[to_str].apply(lambda x:x.astype(pd.StringDtype()))

df['postAt'] = pd.to_datetime(df['postAt'])

df['location'] = df['location'].fillna('NA')
df['work_place'] = df['work_place'].fillna('NA')

rearrange = ['postAt', 'company_name', 'work_place', 'type', 'location']
df = df[rearrange]

df.to_csv(cleaned_data_path, index=False)
print(f"Processed and cleaned csv data has been stored at: '{cleaned_data_path}'.")