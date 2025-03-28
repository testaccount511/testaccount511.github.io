import requests

API_KEY = "JP7RX9NX78XV42RZDKMPLXK5U"

LOCATION = "Henderson, NV"

# API endpoint
URL = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{LOCATION}?unitGroup=us&include=current&key={API_KEY}&contentType=json&include=timezone"


# request
response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    current_temp = data["currentConditions"]["temp"]
    conditions = data["currentConditions"]["conditions"]
    print(f"Current Location: {LOCATION}")
    print(f"Current temperature in {LOCATION} is: {current_temp}°F")
    print(f"Conditions: {conditions}")
    print(f"Time Zone: {data['timezone']}")
else:
    print('Invalid input')
