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

    results = sp.current_user_playing_track()

    song = results['item']['name']
    imageURL = results['item']['album']['images'][2]['url']
    print(song)
    print(imageURL)

    return[song,imageURL]

getAlbumCover()