import json
import requests

import os
from pathlib import Path
from dotenv import dotenv_values

_env = dotenv_values(dotenv_path=Path('.env'))
API_KEY:str = _env.get("API_KEY_SERP")

params = {
    "api_key": API_KEY,
    "q": "keyword here",
    "location": "98146, Washington, United States",
    "gl": "us",
    "hl": "en",
    "google_domain": "google.com"
}

api_result = requests.get("https://api.scaleserp.com/search", params)
print(json.dumps(api_result.json()))
with open("raw-data.json", "w") as outfile:
    json.dump(api_result.json(), outfile, indent=4)
