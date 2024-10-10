import sqlite3
import os
import json

# Define the path to the folder
folder_name = "carbon_registry_data"
current_directory = os.getcwd()
folder_path = os.path.join(current_directory, folder_name)
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS projects (
    id TEXT PRIMARY KEY,
    created_at TEXT,
    updated_at TEXT,
    name TEXT,
    description TEXT,
    status TEXT,
    gsf_standards_version TEXT,
    estimated_annual_credits INTEGER,
    crediting_period_start_date TEXT,
    crediting_period_end_date TEXT,
    methodology TEXT,
    type TEXT,
    size TEXT,
    sustaincert_id INTEGER,
    sustaincert_url TEXT,
    project_developer TEXT,
    carbon_stream TEXT,
    country TEXT,
    country_code TEXT CHECK(length(country_code) = 2),
    latitude REAL,
    longitude REAL,
    state TEXT,
    programme_of_activities TEXT,
    labels TEXT,
    sustainable_development_goals TEXT
);
''')

# List all JSON files in the folder
json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]

len_data = 0
# Open and read each JSON file
for json_file in json_files:
    file_path = os.path.join(folder_path, json_file)
    with open(file_path, 'r') as file:
        data = json.load(file)

    for info in data:
        len_data = len_data + 1
        cursor.execute('''
        INSERT INTO projects (id, created_at, updated_at, name, description, status, gsf_standards_version, estimated_annual_credits,
                                        crediting_period_start_date, crediting_period_end_date, methodology, type, size, sustaincert_id,
                                        sustaincert_url, project_developer, carbon_stream, country, country_code, latitude, longitude,
                                        state, programme_of_activities, labels, sustainable_development_goals)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            info['id'],
            info['created_at'],
            info['updated_at'],
            info['name'],
            info['description'],
            info['status'],
            info['gsf_standards_version'],
            info['estimated_annual_credits'],
            info['crediting_period_start_date'],
            info['crediting_period_end_date'],
            info['methodology'],
            info['type'],
            info['size'],
            info['sustaincert_id'],
            info['sustaincert_url'],
            info['project_developer'],
            info['carbon_stream'],
            info['country'],
            info['country_code'],
            info['latitude'],
            info['longitude'],
            info['state'],
            info['programme_of_activities'],
            json.dumps(info['labels']),  # Convert to JSON string
            json.dumps(info['sustainable_development_goals'])  # Convert to JSON string
        ))

# Commit the changes
conn.commit()

# Query the data
cursor.execute('SELECT count(*) FROM projects')
print(cursor.fetchall()) 

# Close the connection
conn.close()
