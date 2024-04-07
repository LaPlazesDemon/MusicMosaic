import re
import sys

from processors import shazam
from processors import spotify

def is_link(url):
    # Regular expression for URL matching
    youtube_video_regex = r"(?:youtube\.com\/(?:[^/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^\"&?/\s]{11})"
    youtube_regex = r"https?:\/\/music\.youtube\.com\/(?:watch\?v=|embed\/|v\/|)([a-zA-Z0-9_-]{11})"
    spotify_regex = r"https:\/\/open\.spotify\.com\/track\/[a-zA-Z0-9]+"
    apple_regex = r"^https?:\/\/music\.apple\.com\/"
    
    # Check if the provided input matches the URL regex
    if re.search(apple_regex, url):
        return "This is an Apple Music Link"
    elif re.search(spotify_regex, url):
        return "This is a Spotify Link"
    elif re.search(youtube_regex, url):
        return "This is a Youtube Music Link"
    elif re.search(youtube_video_regex, url):
        return "This is a Youtube Video Link"
    else:
        return "No, this is not a link."

if __name__ == "__main__":
    # Check if the user provided an input
    if len(sys.argv) != 2:
        print("Usage: python script.py [URL]")
        sys.exit(1)
    
    # Get the input URL from command line arguments
    url = sys.argv[1]
    shazam.MatchSpotify(url)