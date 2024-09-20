import requests
import csv
import json

# API URL and parameters
url = "https://active-jobs-db.p.rapidapi.com/active-ats"
querystring = {"title": "\"Cyber_security\"", "location": "\"United States\"","description":"text"}

# API Headers
headers = {
    "x-rapidapi-key": "##################",
    "x-rapidapi-host": "active-jobs-db.p.rapidapi.com"
}

# Make the API request
response = requests.get(url, headers=headers, params=querystring)

# Check if the request was successful
if response.status_code == 200:
    job_data = response.json()
    
    # Save data to a JSON file
    with open('job_data.json', 'w') as json_file:
        json.dump(job_data, json_file, indent=4)
    
    # Optionally save data to a CSV file
    if job_data and isinstance(job_data, list):
        with open('job_data.csv', 'w', newline='', encoding='utf-8') as csv_file:
            fieldnames = job_data[0].keys()  # Extract the keys as column headers
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for job in job_data:
                writer.writerow(job)
    
    print("Data saved to job_data.json and job_data.csv")

else:
    print(f"Failed to fetch data. Status code: {response.status_code}")