# MusicMosaic
 A simple to use python project that allows you to input various song links and get the corresponding links to the other streaming services and some basic song data such as duration, title, album, thumbnail art, etc.

### Background
This is a project to get me back into python after not touching it for at least a decade. This is half migrated from a similar Node.JS module

---
# Current Capbilities
At the current moment this is an MVP release. It only accepts a Spotify song link and returns the song data and a link to the same song in Apple Music

**Supported Music Services**
- Spotify

**Planned Music Services**
- YouTube / YouTube Music
- Apple Music
- Tidal[^1]

# Usage
**CLI**
```python
python main.py "<spotify URL>"
```
*Output*
```json
{
    "title": "string",
    "artist": "string",
    "duration": "string",
    "apple_music_link": "uri",
    "spotify_link": "uri"
}
```

I still don't know how to document integrating this library in-script but I plan to make this package ready!

[^1]: If this is even possible, not sure if Tidal even has a web API that allows me to get the data I need
