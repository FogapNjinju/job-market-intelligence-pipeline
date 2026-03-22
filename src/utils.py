import requests


def requesting_job_data(url, headers=None, params=None):
    '''Function to make an API request and return the JSON response.'''
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None