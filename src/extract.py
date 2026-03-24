import os
import serpapi
import utils
from dotenv import load_dotenv  

# Load API key
load_dotenv()
API_KEY = os.getenv("API_KEY")

client = serpapi.Client(api_key=API_KEY)

# === UK Locations ===
uk_locations_tier1 = [
    "London, England, United Kingdom",
    "Birmingham, England, United Kingdom",
    "Manchester, England, United Kingdom",
    "Leeds, England, United Kingdom",
    "Glasgow, Scotland, United Kingdom",
    "Edinburgh, Scotland, United Kingdom"
]

uk_locations_tier2 = [
    "Liverpool, England, United Kingdom",
    "Bristol, England, United Kingdom",
    "Sheffield, England, United Kingdom",
    "Nottingham, England, United Kingdom",
    "Leicester, England, United Kingdom",
    "Coventry, England, United Kingdom",
    "Newcastle upon Tyne, England, United Kingdom",
    "Cardiff, Wales, United Kingdom",
    "Belfast, Northern Ireland, United Kingdom",
    "Swansea, Wales, United Kingdom",
    "Hull, England, United Kingdom",
    "Bradford, England, United Kingdom",
    "Stoke-on-Trent, England, United Kingdom"
]

uk_locations_tier3 = [
    "Reading, England, United Kingdom",
    "Cambridge, England, United Kingdom",
    "Oxford, England, United Kingdom",
    "Milton Keynes, England, United Kingdom",
    "Southampton, England, United Kingdom",
    "Portsmouth, England, United Kingdom",
    "Brighton, England, United Kingdom",
    "Derby, England, United Kingdom",
    "Wolverhampton, England, United Kingdom",
    "York, England, United Kingdom",
    "Exeter, England, United Kingdom",
    "Bath, England, United Kingdom",
    "Newport, Wales, United Kingdom",
    "Aberdeen, Scotland, United Kingdom",
    "Dundee, Scotland, United Kingdom"
]

# === US Locations ===
us_locations_tier1 = [
    "New York, New York, United States",
    "Los Angeles, California, United States",
    "Chicago, Illinois, United States",
    "Houston, Texas, United States",
    "Phoenix, Arizona, United States",
    "Philadelphia, Pennsylvania, United States",
    "San Antonio, Texas, United States",
    "San Diego, California, United States",
    "Dallas, Texas, United States",
    "San Jose, California, United States",
    "Austin, Texas, United States",
    "Jacksonville, Florida, United States",
    "Fort Worth, Texas, United States"
]

us_locations_tier2 = [
    "Columbus, Ohio, United States",
    "San Francisco, California, United States",
    "Charlotte, North Carolina, United States",
    "Indianapolis, Indiana, United States",
    "Seattle, Washington, United States",
    "Denver, Colorado, United States",
    "Washington, District of Columbia, United States",
    "Boston, Massachusetts, United States",
    "El Paso, Texas, United States",
    "Nashville, Tennessee, United States",
    "Detroit, Michigan, United States",
    "Oklahoma City, Oklahoma, United States",
    "Portland, Oregon, United States",
    "Las Vegas, Nevada, United States",
    "Memphis, Tennessee, United States"
]

us_locations_tier3 = [
    "Louisville, Kentucky, United States",
    "Baltimore, Maryland, United States",
    "Milwaukee, Wisconsin, United States",
    "Albuquerque, New Mexico, United States",
    "Tucson, Arizona, United States",
    "Fresno, California, United States",
    "Sacramento, California, United States",
    "Kansas City, Missouri, United States",
    "Mesa, Arizona, United States",
    "Atlanta, Georgia, United States",
    "Omaha, Nebraska, United States",
    "Colorado Springs, Colorado, United States",
    "Raleigh, North Carolina, United States",
    "Miami, Florida, United States",
    "Long Beach, California, United States",
    "Virginia Beach, Virginia, United States",
    "Oakland, California, United States",
    "Minneapolis, Minnesota, United States",
    "Tulsa, Oklahoma, United States"
]

# Combine all locations
all_locations = (
    uk_locations_tier1 + uk_locations_tier2 + uk_locations_tier3 +
    us_locations_tier1 + us_locations_tier2 + us_locations_tier3
)

# Query
query = "Barista"

# Extract jobs
#job_datas = utils.get_jobs_with_serpapi(client, query, all_locations)

title = []
company_name = []
location = []
descriptions = []
job_types = []
share_links = []
qaulifications = []

for city in all_locations:
    jobs = utils.get_jobs_with_serpapi(client, query, [city])
    if jobs:
        for job in jobs:
            print(("=" * 50))
            title.append(job.get('title'))
            company_name.append(job.get('company_name'))
            location.append(job.get('location'))
            descriptions.append(job.get('description'))
            job_types.append(job.get('detected_extensions', {}).get('schedule_type'))
            qaulifications.append(job.get('detected_extensions', {}).get('qualifications'))
            share_links.append(job.get('share_link'))



# Save dataset
#utils.save_to_json(job_datas)