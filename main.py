import requests
import json

uuid = "f0257bcc7d814714abb7e1beb7159b6b"
apiKey = "0cf2a288-fa0d-479c-8b0e-96d7822681c4"

requestLink = f"https://api.hypixel.net/player?key={apiKey}%uuid={uuid}"
def call(api):
    resp = requests.get(api)
    print(resp.json())
print(apiKey)
call(requestLink)