from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

scope = 'user-read-currently-playing'
auth = SpotifyOAuth(scope=scope, open_browser=False)
token = auth.get_access_token()