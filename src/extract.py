import os
import json
import requests
import utils
from dotenv import load_dotenv  


## Loading API key from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")


## Constructing the API URL with the API key
url = f"https://serpapi.com/search?engine=google&q=AI+jobs&api_key={API_KEY}"


## Making the API request
job_data = utils.requesting_job_data(url)


## Saving the data to a JSON file
utils.save_to_json(job_data) 

