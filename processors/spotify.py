from config import config
from processors import shazam

import requests # type: ignore
import base64

access_token = None

# Pull Track ID from a full URL and remove query parameters
def extractTrackId(song_url):
    path_and_params = song_url.split("?")[0]
    parts = path_and_params.split("/")
    index = parts.index("track")
    track_id = parts[index + 1]
    return track_id


# Download the 30 second preview from Spotify (will need to be further trimmed)
def downloadSongPreview(url):
    
    track_id = extractTrackId(url)
    previewUrl = getTrackDetails(track_id);

    response = requests.get(previewUrl)
    if response.status_code == 200:
        return response.content
    else:
        print("Failed to download audio. Status code:", response.status_code)
        return False

# Retrieve the Preview URL using the Spotify Web API
def getTrackDetails(track_id):
    response = requests.get(f"https://api.spotify.com/v1/tracks/{track_id}", headers={"Authorization": f"Bearer {access_token}"})
    data = response.json()
    return data["preview_url"]


# Retrieve a new access token using the refresh token
def getToken():

    global access_token

    restUri = "https://accounts.spotify.com/api/token"
    clientCreds = base64.b64encode(f"{config.spotify['clientId']}:{config.spotify['key']}".encode()).decode()

    requestData = {
        "grant_type": "refresh_token",
        "refresh_token": config.spotify['refreshToken']
    }
    
    headers = {
        "Authorization": f"Basic {clientCreds}"
    }
    
    response = requests.post(restUri, data=requestData, headers=headers)

    if response.status_code == 200:
        access_token = response.json()["access_token"]
    else:
        print("Error getting new Spotify Token:", response.text)


getToken()