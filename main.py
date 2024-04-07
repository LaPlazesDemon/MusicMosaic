import re
import sys

from processors import shazam
from processors import spotify

youtube_video_regex = r"(?:youtube\.com\/(?:[^/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^\"&?/\s]{11})"
youtube_regex = r"https?:\/\/music\.youtube\.com\/(?:watch\?v=|embed\/|v\/|)([a-zA-Z0-9_-]{11})"
spotify_regex = r"https:\/\/open\.spotify\.com\/track\/[a-zA-Z0-9]+"
apple_regex = r"^https?:\/\/music\.apple\.com\/"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py [URL]")
        sys.exit(1)
    
    url = sys.argv[1]

    if re.search(spotify_regex, url):
        shazam.MatchSpotify(url)
    else:
        print("Sorry that streaming service is not supported or the URL is malformed")
        sys.exit(1)