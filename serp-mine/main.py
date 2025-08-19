import json
import requests

from pathlib import Path
from dotenv import dotenv_values

# Securiser la clee API dans un fichier .env
_env = dotenv_values(dotenv_path=Path('.env'))
API_KEY:str = _env.get("API_KEY_SERP")

# Variables du sujet
key_word:str = "domino’s pizza"
location:str = "Paris,Paris,Ile-de-France,France"
device:str = "mobile"
page:int = 1
result_page:int = 20

# Doc : https://docs.trajectdata.com/scaleserp/search-api/searches/google/search
# La doc contient la liste des parametres du endpoint avec des descriptions sur l'effet et la nature de la variable.
params = {
    "api_key": API_KEY,
    "q": key_word,
    "location": location,
    "page" : page,
    "num": result_page,
    "device_type" : device,
    "google_domain": "google.com",
}

# On fait un get sur l'endpoint search, puis on recup le json de la reponse et on sauvegarde en local.
# C'est la library json qui s'occupe de dump le dict dans le fichier que l'on init.
api_result = requests.get("https://api.scaleserp.com/search", params)
with open("resultats.json", "w") as outfile:
    json.dump(api_result.json(), outfile, indent=4)
