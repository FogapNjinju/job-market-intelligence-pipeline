import requests
import os
import json

def requesting_job_data(url, headers=None, params=None):
    '''Function to make an API request and return the JSON response.'''
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    

    
def save_to_json(data):
    '''Function to save data to a JSON file.'''
    try:
        os.makedirs("../data/raw", exist_ok=True)

        with open('../data/raw/job_data.json', 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data successfully saved to ../data/raw/job_data.json") 
    except IOError as e:
        print(f"An error occurred while saving to file: {e}")


def load_from_json(file_path):
    '''Function to load data from a JSON file.'''
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except IOError as e:
        print(f"An error occurred while loading from file: {e}")
        return None
    

def get_jobs_with_serpapi(client, query, location):
    '''Function to get job listings using SerpAPI.'''
    try:
        results = client.search({
            "engine": "google_jobs",
            "q": query,
            "location": location,
            "google_domain": "google.com",
            "hl": "en",
            "gl": "us"
        })
        return results.get("jobs_results", [])
    except Exception as e:
        print(f"An error occurred while fetching jobs: {e}")
        return []
    

def transform_jobs(data: list) -> dict:
    """
    Transform raw job data into structured lists
    """
    titles = []
    company_names = []
    locations = []
    descriptions = []
    job_types = []

    for job in data:
        titles.append(job.get('title'))
        company_names.append(job.get('company_name'))
        locations.append(job.get('location'))
        descriptions.append(job.get('description'))

        job_types.append(
            job.get('detected_extensions', {}).get('schedule_type')
        )

    return {
        "title": titles,
        "company_name": company_names,
        "location": locations,
        "description": descriptions,
        "job_type": job_types
    }

def separate_city_country(location):
    '''Function to separate city and country from a location string.'''
    try:
        parts = location.split(", ")
        if len(parts) >= 2:
            city = parts[0]
            country = parts[-1]
            return city, country
        else:
            return location, None
    except Exception as e:
        print(f"An error occurred while separating city and country: {e}")
        return location, None