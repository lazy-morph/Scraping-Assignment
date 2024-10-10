# import time
# import requests
# import os
# import json

# pages = 139
# headers = {
#     "accept": "application/json, text/plain, */*",
#     "accept-encoding": "gzip, deflate, br",
#     "accept-language": "en-GB,en;q=0.9",
#     "cache-control": "no-cache",
#     "origin": "https://registry.goldstandard.org",
#     "pragma": "no-cache",
#     "priority": "u=1, i",
#     "referer": "https://registry.goldstandard.org/",
#     "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Brave";v="128"',
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": '"macOS"',
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-site",
#     "sec-gpc": "1",
#     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
# }

# # Define the name of the new folder
# folder_name = "carbon_registry_data"

# # Get the current directory
# current_directory = os.getcwd()

# # Create the full path for the new folder
# new_folder_path = os.path.join(current_directory, folder_name)

# # Check if the folder already exists
# if not os.path.exists(new_folder_path):
#     # Create the new folder
#     os.makedirs(new_folder_path)
#     print(f"Folder '{folder_name}' created at {new_folder_path}.")
# else:
#     print(f"Folder '{folder_name}' already exists at {new_folder_path}.")


# for i in range(1,pages+1):
#     # time.sleep(10)
#     flag = False
#     url = f"https://public-api.goldstandard.org/projects?query=&page={i}&size=25&sortColumn=&sortDirection="
#     for j in range(5):
#         time.sleep(2)
#         try:
#             res = requests.get(url, headers=headers)

#             if res.status_code == 200:
#                 data = res.json()
#                 json_file_path = os.path.join(new_folder_path, f"page_{i}.json")

#                 with open(json_file_path, 'w') as json_file:
#                     json.dump(data, json_file, indent=4, ensure_ascii=False)

#                 flag = True
            
#             if flag:
#                 print(f"Page {i} scraping successful.")
#                 break

#         except Exception as e:
#             print(e)

# from requests_html import HTMLSession
# from bs4 import BeautifulSoup as soup

# # Create an HTML session
# session = HTMLSession()

# # Specify the URL
# url = 'https://registry.goldstandard.org/projects?q=&page=1'  # Replace with your URL

# # Send a GET request
# response = session.get(url)

# # Render the JavaScript
# response.html.render(sleep=5,keep_page=True,scrolldown=1)

# # Print the complete HTML response after rendering JavaScript
# r = response.html.html

# res = soup(r,"html.parser")

# # print(res)

# page_no = res.find("div",{"id": "root"})

# print(page_no)

# # Optionally, close the session
# session.close()

import asyncio
from playwright.async_api import async_playwright

async def fetch_and_render(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch()  # You can use .firefox or .webkit as well
        page = await browser.new_page()
        
        # Navigate to the URL
        await page.goto(url,timeout=50000)

        # Wait for the content to load (adjust the timeout as necessary)
        await page.wait_for_timeout(5000)  # Wait for 5 seconds

        # Get the full HTML content
        content = await page.content()

        # Close the browser
        await browser.close()
        
        return content

# Example usage
url = 'https://registry.goldstandard.org/projects?q=&page=1'  # Replace with your actual URL

# Run the async function
html_content = asyncio.run(fetch_and_render(url))

# Print the rendered HTML
print(html_content)

# print(html_content.find("div",{"id": "root"}))





