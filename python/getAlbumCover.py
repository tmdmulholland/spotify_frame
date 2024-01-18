from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.current_user_playing_track()

print(results)

song = results['item']['album']
imageURL = results['item']['album']['images'][2]['url']
print(song)
print(imageURL)