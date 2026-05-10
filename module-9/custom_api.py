"""
    Author:      Zachary White
    Instructor:  Darrell Payne
    Date:        05/10/2026
    Assignment:  Module 9 - Working with APIs in Python
    Description: Custom API program that uses the Open Notify ISS Location API
                 (http://api.open-notify.org/iss-now.json) to retrieve the
                 current real-time position of the International Space Station.
                 No API key is required. The program tests the connection,
                 prints the raw JSON response, then displays formatted output
                 showing the ISS latitude, longitude, and timestamp.
"""

import requests
from datetime import datetime

print("=" * 55)
print("Custom API Program - ISS Current Location")
print("=" * 55)

# -------------------------------------------------------
# Step 1: Test the API connection
# -------------------------------------------------------
print("\nSTEP 1: Testing API Connection")
print("-" * 40)

base_url = "http://api.open-notify.org/iss-now.json"
test_response = requests.get(base_url)
print(f"Connection status code: {test_response.status_code}")

if test_response.status_code == 200:
    print("Connection successful!")
else:
    print("Connection issue - check the URL or network.")

# -------------------------------------------------------
# Step 2: Make the API request for ISS position
# -------------------------------------------------------
print("\nSTEP 2: Fetching Current ISS Position")
print("-" * 40)

iss_url = "http://api.open-notify.org/iss-now.json"
response = requests.get(iss_url)
print(f"ISS API status code: {response.status_code}")

# -------------------------------------------------------
# Step 3: Print raw (unformatted) response
# -------------------------------------------------------
print("\nSTEP 3: Raw (Unformatted) Response:")
print("-" * 40)
print(response.text)

# -------------------------------------------------------
# Step 4: Print formatted response
# -------------------------------------------------------
print("\nSTEP 4: Formatted Output:")
print("=" * 55)

data = response.json()

# Convert Unix timestamp to readable date/time
timestamp  = data["timestamp"]
readable   = datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S UTC")
latitude   = data["iss_position"]["latitude"]
longitude  = data["iss_position"]["longitude"]

print(f"  Status     : {data['message']}")
print(f"  Timestamp  : {timestamp}  ({readable})")
print(f"  Latitude   : {latitude}")
print(f"  Longitude  : {longitude}")
print(f"  Track ISS  : https://www.n2yo.com/passes/")

print("=" * 55)
print("Program complete.")