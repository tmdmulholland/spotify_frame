from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# def getToken():
scope = 'user-read-currently-playing'

    # This way removes the need for a browser, it will instead give the URL to visit in the terminal
    # auth = SpotifyOAuth(scope=scope, open_browser=False)
    # token = auth.get_access_token()


auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

now_playing = sp.current_user_playing_track()