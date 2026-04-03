from pathlib import Path
import utils


def main():
   # Get current file path
   current_file = Path(__file__).resolve()

   # Navigate to project root → then to data/raw/file.json
   data_path = current_file.parents[1] / "data" / "raw" / "job_data.json"

   # Load the JSON data
   raw_data = utils.load_from_json(data_path)

   if raw_data is None:
       print("No data to transform")
       return

   location = raw_data.get('location', [])
   title = raw_data.get('title', [])
   company_name = raw_data.get('company_name', [])
   descriptions = raw_data.get('description', [])
   job_types = raw_data.get('job_type', [])
   qualifications = raw_data.get('qualifications', [])
   share_links = raw_data.get('share_link', [])

   ## cleaning of location
   ## remove duplicate locations - but actually, we need to keep them aligned with other fields
   # unique_locations = list(set(location))

   ## seperate city, country
   cities = [] 
   countries = []

   for loc in location:
      city, country = utils.separate_city_country(loc)
      cities.append(city)
      countries.append(country)

   ## cleaning of descriptions
   # descriptions = utils.clean_descriptions(descriptions)  # This removes duplicates, but we need to keep aligned

   # For now, just clean individual descriptions
   cleaned_descriptions = []
   for desc in descriptions:
       if desc:
           desc = desc.strip()
           cleaned_descriptions.append(desc)
       else:
           cleaned_descriptions.append("")

   # Save transformed data
   transformed_data = {
       'title': title,
       'company_name': company_name,
       'city': cities,
       'country': countries,
       'description': cleaned_descriptions,
       'job_type': job_types,
       'qualifications': qualifications,
       'share_link': share_links
   }

   processed_path = current_file.parents[1] / "data" / "processed" / "transformed_job_data.json"
   utils.save_to_json(transformed_data, processed_path)

if __name__ == "__main__":
    main()