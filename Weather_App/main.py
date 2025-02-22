import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key securely
api_key1 = os.getenv("api_key")


# get user input for city name
city = input("Enter city name: ")

# construct the api url
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key1}&units=metric"


try:
    # Send the request
    r = requests.get(url)
    r.raise_for_status()  # Raise an error for HTTP issues

    # Parse JSON response
    wdic = r.json()
    w = wdic['main']['temp']

    # Print formatted temperature
    print(f"{w}°C")

except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
except KeyError:
    print("Invalid city name or missing data!")