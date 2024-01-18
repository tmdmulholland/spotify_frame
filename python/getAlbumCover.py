import os
from dotenv import load_dotenv

load_dotenv()

# spotipy_client_id = os.getenv('CLIENT_ID')
# spotipy_client_secret = os.getenv('CLIENT_SECRET')
# spotipy_redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])