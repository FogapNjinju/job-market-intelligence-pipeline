import os
import serpapi
import utils
import json
from dotenv import load_dotenv
from pathlib import Path


def main():
    # Load API key
    load_dotenv()
    API_KEY = os.getenv("API_KEY")

    if not API_KEY:
        raise ValueError("API_KEY not found in environment variables")

    client = serpapi.Client(api_key=API_KEY)

    # Load configuration
    config_path = Path(__file__).parent.parent / "config" / "config.json"
    with open(config_path, 'r') as f:
        config = json.load(f)

    query = config.get("query", "Barista")
    locations_config = config.get("locations", {})

    # Combine all locations
    all_locations = []
    for tier, locations in locations_config.items():
        all_locations.extend(locations)

    # Extract jobs
    title = []
    company_name = []
    location = []
    descriptions = []
    job_types = []
    share_links = []
    qualifications = []

    for city in all_locations:
        jobs = utils.get_jobs_with_serpapi(client, query, [city], config.get("max_retries", 5), config.get("base_delay", 2))
        if jobs:
            for job in jobs:
                print(f"Processing job in {city}")
                title.append(job.get('title', ''))
                company_name.append(job.get('company_name', ''))
                location.append(job.get('location', ''))
                descriptions.append(job.get('description', ''))
                job_types.append(job.get('detected_extensions', {}).get('schedule_type', ''))
                qualifications.append(job.get('detected_extensions', {}).get('qualifications', ''))
                share_links.append(job.get('share_link', ''))

    # Save dataset
    job_data = {
        'title': title,
        'company_name': company_name,
        'location': location,
        'description': descriptions,
        'job_type': job_types,
        'qualifications': qualifications,
        'share_link': share_links
    }
    output_path = Path(__file__).parent.parent / "data" / "raw" / "job_data.json"
    utils.save_to_json(job_data, str(output_path))

if __name__ == "__main__":
    main()