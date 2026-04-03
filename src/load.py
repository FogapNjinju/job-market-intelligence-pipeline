import utils
import sqlite3
import os
from pathlib import Path


def main():
    # Get current file path
    current_file = Path(__file__).resolve()
    processed_path = current_file.parents[1] / "data" / "processed" / "transformed_job_data.json"

    # Load transformed data
    transformed_data = utils.load_from_json(processed_path)

    if transformed_data is None:
        print("No transformed data to load")
        return

    ## connect to database directory and file
    db_dir = current_file.parents[1] / "data" / "processed"
    db_dir.mkdir(parents=True, exist_ok=True)
    db_path = db_dir / 'job_data.db'

    conn = sqlite3.connect(str(db_path))

    ## create a cursor object to execute SQL commands
    cursor = conn.cursor()

    ## create a table to store the data
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS job_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company_name TEXT,
            city TEXT,
            country TEXT,
            description TEXT,
            job_type TEXT,
            qualifications TEXT,
            share_link TEXT
        )
    ''')

    ## creating a list of tuples to insert into the database
    data_to_insert = list(zip(
        transformed_data.get('title', []),
        transformed_data.get('company_name', []),
        transformed_data.get('city', []),
        transformed_data.get('country', []),
        transformed_data.get('description', []),
        transformed_data.get('job_type', []),
        transformed_data.get('qualifications', []),
        transformed_data.get('share_link', [])
    ))

    ## insert the data into the database
    cursor.executemany('''
        INSERT INTO job_data (title, company_name, city, country, description, job_type, qualifications, share_link)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', data_to_insert)

    ## commit the changes and close the connection
    conn.commit()
    conn.close()

    print(f"Data loaded into {db_path}")

if __name__ == "__main__":
    main()
    conn.close()

if __name__ == "__main__":
    main()