from pathlib import Path
import json
import utils
import extract

# Get current file path (clean.py)
current_file = Path(__file__).resolve()

# Navigate to project root → then to data/raw/file.json
data_path = current_file.parents[1] / "data" / "raw" / "job_data.json"

# Load the JSON data
raw_data1 = utils.load_from_json(data_path)

# Define variable to hold transformed data
location = extract.location
title = extract.title
company_name = extract.company_name
descriptions = extract.descriptions
job_types = extract.job_types

## cleaning of location
## remove duplicate locations
unique_locations = list(set(location))



## seperate city, country
cities = [] 
countries = []

for loc in location:
   city, country = utils.separate_city_country(loc)
   cities.append(city)
   countries.append(country)


