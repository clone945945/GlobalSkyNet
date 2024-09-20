![pexels-tara-winstead-8386440](https://github.com/user-attachments/assets/70ba4273-ebff-44de-ae58-d0fcc1d54395)



# Introduction
* This Python script is designed to fetch job data from the Active Jobs API and save the data in both JSON and CSV formats. The API allows you to search for jobs based on specific titles and locations. The script demonstrates how to handle API requests, parse the response, and store the data effectively in a structured format.

# API URL and Parameters
* The **API URL** used to fetch the data is:
[Active Jobs API](https://active-jobs-db.p.rapidapi.com/active-ats)

The **querystring** parameters are as follows:
<!-- Python block -->

```python
{
    "title": "\"Cyber_Security\"",
    "location": "\"United States\""
}
```

* These parameters define the **job title** and **location** we are searching for.

# API Headers
<!-- Python block -->
```python
headers = {
    "x-rapidapi-key": "your_api_key_here",
    "x-rapidapi-host": "active-jobs-db.p.rapidapi.com"}
```
* **Important:** Make sure to replace `Your_API_Key_Here` with your actual **API key**.

# Making the API Request
* The following code sends a **GET request** to the API with the defined **URL**, **headers**, and **query parameters**:
<!-- Python block -->
```python
response = requests.get(url, headers=headers, params=querystring)

```
* This request is processed and returns a response containing job data.

# Handling the Response
* After making the request, the response status is checked to ensure the request was successful:
<!-- Python block -->
```python
if response.status_code == 200:
    job_data = response.json()
```
* If the response is successful (status code **200**), the data is converted into a **JSON object**.

# Saving Data to JSON
* Once the data is retrieved, it is saved into a **JSON file** for further analysis:
 <!-- Python block -->

```python
with open('job_data.json', 'w') as json_file:
    json.dump(job_data, json_file, indent=4)
```
* This ensures the data is formatted and easily readable.
# **Saving Data to CSV**
*To save the data in a **CSV file***, the script checks if the data is a list, extracts fieldnames, and writes it into the file:
<!-- Python block -->

```python
if job_data and isinstance(job_data, list):
    with open('job_data.csv', 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = job_data[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for job in job_data:
            writer.writerow(job)
```
* This makes the data easier to handle in spreadsheet applications.

# Error Handling
In case of a failed request, the script will notify you with the **status code**:
 <!-- Python block -->

```python
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
```
# Inline code block
* Here is an example of the inline code block: `<p>Cyber_Security Jobs</p>`

# Task List
 * Fetch job data from API
   
 * Save data to JSON
   
 * Save data to CSV
   
 * Handle other job titles and locations
# Images
Here is an image representing the *data extraction** process:
![Excel](https://github.com/user-attachments/assets/b15d4f4f-1688-4eed-a6d6-aff73c093c90)


# Tips
Here are some **awesome tips** for improving this code:
* *Parameterize the search inputs*: Allow users to dynamically choose job titles or locations.
* *Handle pagination*: If the API returns a large amount of data, handle multiple pages.
* *Logging:* Add logging to track the API requests and responses.

# More awesome tips!
* Add a user interface for easier job searches.
* Schedule regular API calls to keep job data up-to-date.
