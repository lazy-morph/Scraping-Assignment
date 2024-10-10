import time
import requests
import os
import json

pages = 139  # This page no has been hardcoded because the website is using javascript rendering for loading the content. Otherwise the info is hidden.
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-GB,en;q=0.9",
    "cache-control": "no-cache",
    "origin": "https://registry.goldstandard.org",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://registry.goldstandard.org/",
    "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Brave";v="128"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
}

# Define the name of the new folder
folder_name = "carbon_registry_data"

# Get the current directory
current_directory = os.getcwd()

# Create the full path for the new folder
new_folder_path = os.path.join(current_directory, folder_name)

# Check if the folder already exists
if not os.path.exists(new_folder_path):
    # Create the new folder
    os.makedirs(new_folder_path)
    print(f"Folder '{folder_name}' created at {new_folder_path}.")
else:
    print(f"Folder '{folder_name}' already exists at {new_folder_path}.")


for i in range(
    1, pages + 1
):  # This for loop will run for all the pages on the website.
    flag = False
    url = f"https://public-api.goldstandard.org/projects?query=&page={i}&size=25&sortColumn=&sortDirection="  # openapi to get the project details from the pages
    for j in range(5):  # This for loop is for retrying a url for upto 5 times.
        time.sleep(
            2
        )  # This sleep is to slow down the traffic that reaches website from the current IP. had to be done as after some pages there was too many requests error popping up.
        try:
            res = requests.get(url, headers=headers)  # Make request to the API url.

            if (
                res.status_code == 200
            ):  # If the request is successful then extract the json and dump into the folder.
                data = res.json()
                json_file_path = os.path.join(new_folder_path, f"page_{i}.json")

                with open(json_file_path, "w") as json_file:
                    json.dump(data, json_file, indent=4, ensure_ascii=False)

                flag = True

            if flag:
                print(f"Page {i} scraping successful.")
                break

        except Exception as e:
            print(e)


# https://public-api.goldstandard.org/projects/4653
# This url can be used to get the project information directly using the project code.
# But the same information is also present on the projects page for each project hence not using this url to limit the number of requests.
