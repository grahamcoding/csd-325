# Daniel Graham
# Date: 7/4/25
# Module 8.2 Assignment: API Practice

import requests
import json

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu/")
data = response.json()
print(json.dumps(data, indent=4))