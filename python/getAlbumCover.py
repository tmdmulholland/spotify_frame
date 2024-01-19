from dotenv import load_dotenv
import spotipy
import spotipy.util as util

load_dotenv()

token_path = '.cache'
scope = 'user-read-currently-playing'
username = 'Tom'

def getAlbumCover():

    token = util.prompt_for_user_token(username, scope, cache_path=token_path)

    sp = spotipy.Spotify(auth=token)

    currentData = sp.current_user_playing_track()

    if currentData is None:
        return
    else:
        song = currentData['item']['name']
        imageURL = currentData['item']['album']['images'][0]['url']
        return[song, imageURL]