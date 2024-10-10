# Calyx_Global_Assignment
Repository for Calyx Global Assignment

For running this code clone the repository to your local machine.
Please make sure that python3 is installed in the system.

Once the cloning is done, can follow these steps:
1. Run the scrape.py file with command python3 scrape.py. This file will create a folder by the name carbon_registry_data and dump the page jsons one by one with the filename as page_{no}.json.
2. After this run the ingest.py file which will create a local database by the name data.db and with a table by the name of projects which will contain all the projects information.
3. The ingest.py file will read the files one by one from the carbon_registry_data folder and ingest all the information in the database.
4. The query_db.py file is just for running a simple select query on the database which returns the first row.

