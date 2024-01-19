from getAlbumCover import getAlbumCover
from PIL import Image
import requests
from io import BytesIO

prevSong    = ""
currentSong = ""

imageURL = getAlbumCover()
imageURL = imageURL[1]

response = requests.get(imageURL)
img = Image.open(BytesIO(response.content))