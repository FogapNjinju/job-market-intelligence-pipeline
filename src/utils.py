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