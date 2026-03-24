import transform
import utils
import extract
import sqlite3
import os


def main():
    ## connect to database directory and file
    db_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'processed'))
    os.makedirs(db_dir, exist_ok=True)
    db_path = os.path.join(db_dir, 'job_data.db')
    conn = sqlite3.connect(db_path)

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
            share_link TEXT '''
        )   

    ## creating a list of tuples to insert into the database
    data_to_insert = list(zip(transform.title, transform.company_name, transform.cities, transform.countries, transform.descriptions, transform.job_types, transform.qualifications, transform.share_links))

    ## insert the data into the database
    cursor.executemany('''
        INSERT INTO job_data (title, company_name, city, country, description, job_type, qualifications, share_link)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', data_to_insert)


    ## print out database entries to verify
    cursor.execute('SELECT * FROM job_data')
    rows = cursor.fetchall()
    for row in rows:
        print(row)


    ## commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()