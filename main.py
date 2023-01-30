import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

NUTRI_API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRI_API_HEADER = {
    "x-app-id": os.environ.get("NUTRI_API_ID"),
    "x-app-key": os.environ.get("NUTRI_API_KEY"),
}
SHEETY_API_HEADER = {
    "Authorization": os.environ.get("SHEETY_API_KEY"),
}

nutri_api_parameters = {
    "query": input("What do You want to tell me?: "),
    "gender": "male",
    "weight_kg": 78,
    "height_cm": 183,
    "age": 25
}
response_nutri = requests.post(url=NUTRI_API_ENDPOINT, json=nutri_api_parameters, headers=NUTRI_API_HEADER)
data = response_nutri.json()

today = datetime.now()
today_date_formatted = today.strftime("%d/%m/%Y")
today_time_formatted = today.strftime("%X")

for exercise in data["exercises"]:
    name = exercise["name"]
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]
    sheety_api_parameters = {
        "workout": {
            "date": today_date_formatted,
            "time": today_time_formatted,
            "exercise": name,
            "duration": duration,
            "calories": calories,
        }
    }

    response_sheety = requests.post(url=os.environ.get("SHEETY_API_ENDPOINT"), json=sheety_api_parameters,
                                    headers=SHEETY_API_HEADER)
