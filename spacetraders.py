import json
import random
import requests

callsign = f"jotingen{random.getrandbits(32)}"[0:13]
headers = {
    "Content-Type": "application/json",
}
url_register = "https://api.spacetraders.io/v2/register"
data = {
    "symbol": callsign,
    "faction": "COSMIC",
}
response = requests.post(url_register, headers=headers, data=json.dumps(data))
print(response.text)
