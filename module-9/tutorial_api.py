"""
    Author:      Zachary White
    Instructor:  Darrell Payne
    Date:        05/08/2026
    Assignment:  Module 9 - Working with APIs in Python
    Description: Tutorial program that tests an HTTP connection to google.com
                 and then calls the Open Notify API (http://api.open-notify.org)
                 to retrieve and display the names and spacecraft of all
                 astronauts currently in space, in both raw and formatted output.
"""
 


import requests
import json

# -------------------------------------------------------
# Step 1: Test the connection
# -------------------------------------------------------
print("=" * 50)
print("STEP 1: Testing API Connection")
print("=" * 50)

response = requests.get('http://www.google.com')
print(f"Google status code: {response.status_code}")  # 200 = OK

# -------------------------------------------------------
# Step 2: Retrieve current astronauts in space
# -------------------------------------------------------
print("\n" + "=" * 50)
print("STEP 2: Current Astronauts in Space")
print("=" * 50)

astros_url = "http://api.open-notify.org/astros.json"
response = requests.get(astros_url)

print(f"Astronauts API status code: {response.status_code}")
print("\nRaw (unformatted) response:")
print(response.text)

# Parse and format the response
data = response.json()

print("\nFormatted Output:")
print(f"Number of people in space: {data['number']}")
print("\nAstronauts currently in space:")
print("-" * 30)
for person in data['people']:
    print(f"  Name:  {person['name']}")
    print(f"  Craft: {person['craft']}")
    print("-" * 30)
