import requests
import json

url = "https://linkedin-data-api.p.rapidapi.com/search-jobs-v2"

querystring = {
    "keywords": "python",
    "locationId": "102713980",
    "datePosted": "anyTime",
    "sort": "mostRelevant"
}

headers = {
    "x-rapidapi-key": "cafc3459fcmsh57b25e3bf42316ep19a521jsn572d50692ea8",
    "x-rapidapi-host": "linkedin-data-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# Assuming the response is JSON, store it in a variable
data = response.json()

# Specify the file path where you want to save the JSON data
file_path = "/home/vignesh-nadar/Desktop/sixtyDays/sprint1/project1/data/raw_data/raw_data.json"

# Open the file in write mode and save the JSON data
with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)

print(f"Data saved to {file_path}")

