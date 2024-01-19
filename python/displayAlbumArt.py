from getAlbumCover import getAlbumCover
from PIL import Image
import requests
from io import BytesIO
import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions
import spotipy


options = RGBMatrixOptions()
options.rows = 64
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat-pwm'
options.gpio_slowdown = 0
# options.gpio_slowdown = 1
# options.gpio_slowdown = 2
options.brightness = 50
options.limit_refresh_rate_hz = 10

matrix = RGBMatrix(options = options)


lastSong = ""
currentSong = ""

try:
    while True:
        currentSongData = getAlbumCover()
        imageURL = currentSongData[1]
        currentSong = currentSongData[0]
        if currentSong != lastSong:
            lastSong = currentSong
            response = requests.get(imageURL)
            img = Image.open(BytesIO(response.content))
            img.show()
            img.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
            print(currentSong)
        else:
            print('same song')

        matrix.SetImage(img.convert('RGB'))
        time.sleep(0.5)

except:
    print('nothing playing'10
    time.sleep(1)

