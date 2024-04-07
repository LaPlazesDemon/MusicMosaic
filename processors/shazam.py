from config import config

from processors import audio
from processors import spotify
import base64
import requests # type: ignore

def SendShazamRequeset(song_buffer):

    url = "https://shazam.p.rapidapi.com/songs/v2/detect"
    params = {"timezone": "America/Chicago","locale": "en-US"}
    headers = {
        "content-type": "text/plain",
        "X-RapidAPI-Key": config.shazam['key'],
        "X-RapidAPI-Host": "shazam.p.rapidapi.com"
    }
    data = base64.b64encode(song_buffer)
    
    response = requests.post(url, params=params, headers=headers, data=data)
    if response.status_code == 200:
        return response


    else:
        print("Error:", response.status_code)


def MatchSpotify(url):
    mp3PreviewAudio = spotify.downloadSongPreview(url)
    previewBuffer = audio.convert_encode_mp3(mp3PreviewAudio)
    response = SendShazamRequeset(previewBuffer)

    trackInformation = response.json()['track']
    openInformation = next((option for option in trackInformation['hub']['options'] if option.get("caption") == "OPEN"), None)
    appleMusicOpenInformation = next((action for action in openInformation['actions'] if action.get("type") == "applemusicopen"), None)

    songTitle = trackInformation['title']
    songArtist = trackInformation['subtitle']
    appleMusicOpenLink = appleMusicOpenInformation['uri']

    output = {
        "title": songTitle,
        "artist": songArtist,
        "apple_music_link": appleMusicOpenLink,
        "spotify_link": f"https://open.spotify.com/track/{spotify.extractTrackId(url)}"
    }

    print(output)

