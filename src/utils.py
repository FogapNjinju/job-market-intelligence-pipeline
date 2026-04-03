import requests
import os
import json
import re
import time
import random


def requesting_job_data(url, headers=None, params=None):
    '''Function to make an API request and return the JSON response.'''
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    

    
def save_to_json(data, file_path):
    '''Function to save data to a JSON file.'''
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data successfully saved to {file_path}") 
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
    

def get_jobs_with_serpapi(client, query, location, max_retries=5, base_delay=2):
    '''Function to get job listings using SerpAPI with retry/backoff for 429 rate limits.'''

    if isinstance(location, list):
        if len(location) == 1:
            location_value = location[0]
        else:
            location_value = ", ".join(location)
    else:
        location_value = location

    attempt = 1
    while attempt <= max_retries:
        try:
            results = client.search({
                "engine": "google_jobs",
                "q": query,
                "location": location_value,
                "google_domain": "google.com",
                "hl": "en",
                "gl": "us"
            })
            # gentle pacing to reduce rate-limits
            time.sleep(1)
            return results.get("jobs_results", [])
        except Exception as e:
            message = str(e)
            is_rate_limit = "429" in message or "Too Many Requests" in message
            if attempt == max_retries:
                print(f"An error occurred while fetching jobs (final attempt): {e}")
                return []
            delay = base_delay * (2 ** (attempt - 1)) + random.uniform(0, 1)
            if is_rate_limit:
                print(f"Rate limit hit (429) for location '{location_value}'. retry {attempt}/{max_retries} in {delay:.1f}s")
            else:
                print(f"Fetch error for location '{location_value}'. retry {attempt}/{max_retries} in {delay:.1f}s: {e}")
            time.sleep(delay)
            attempt += 1

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
    

def clean_descriptions(descriptions):
    cleaned = set()

    for text in descriptions:
        if not text:
            continue

        # Normalize formatting
        text = re.sub(r'\n+', ' ', text)   # remove newlines
        text = re.sub(r'\s+', ' ', text)   # remove extra spaces
        text = re.sub(r'•', '', text)      # remove bullet points

        text = text.strip().lower()

        cleaned.add(text)  # set removes duplicates

    return list(cleaned)