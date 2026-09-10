import requests
import json

# Example API call
lyric = requests.get("https://example.com")

# Ensure the request succeeded before parsing
if lyric.status_code == 200:
    lyrics = lyric.json()
    print(lyrics)
else:
    print(f"Failed to fetch lyrics. Status code: {lyric.status_code}")
