import json
import requests

import os
from pathlib import Path
from dotenv import dotenv_values

_env = dotenv_values(dotenv_path=Path('.env'))
API_KEY:str = _env.get("API_KEY_SERP")

key_word:str = "domino’s pizza"
location:str = "Paris,Paris,Ile-de-France,France"
device:str = "mobile"
page:int = 1
result_page:int = 20

# Doc : https://docs.trajectdata.com/scaleserp/search-api/searches/google/search
params = {
    "api_key": API_KEY,
    "q": key_word,
    "location": location,
    "page" : page,
    "num": result_page,
    "device_type" : device,
    "google_domain": "google.com",
}

api_result = requests.get("https://api.scaleserp.com/search", params)
with open("resultats.json", "w") as outfile:
    json.dump(api_result.json(), outfile, indent=4)
