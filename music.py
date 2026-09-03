import json
from requests_oauthlib import OAuth1Session
import requests
url =  'https://api.audiomack.com/v1'
response = requests.get(url)
data = response.json()
print(data)