import time
import math
import random
import board
import adafruit_dotstar as dotstar
from PIL import Image, ImageOps

panelCount = 4
panelWidth = 8
panelHeight = 8
panelTotal = panelWidth * panelHeight
dotCount = panelTotal * panelCount
asciiDir = './ascii'

FILENAME = asciiDir + '/' + '48.png'

dots = dotstar.DotStar(
        board.SCK, 
        board.MOSI, 
        dotCount, 
        auto_write=False,
        brightness=0.1
    )

IMG_RAW = Image.open(FILENAME).convert("RGB")
IMG = ImageOps.invert(IMG_RAW)
PIXELS = IMG.load()
WIDTH = IMG.size[0]
HEIGHT = IMG.size[1]
print("%dx%d pixels" % IMG.size)


print("Allocating...")
COLUMN = [0 for x in range(WIDTH)]
for x in range(WIDTH):
    COLUMN[x] = [[0, 0, 0, 0] for _ in range(HEIGHT)]

print("Converting...")
for x in range(WIDTH):  # For each column of image
    for y in range(HEIGHT):  # For each pixel in column
        value = PIXELS[x, y]  # Read RGB pixel in image
        COLUMN[x][y][0] = value[0]  # Gamma-corrected R
        COLUMN[x][y][1] = value[1]  # Gamma-corrected G
        COLUMN[x][y][2] = value[2]  # Gamma-corrected B
        COLUMN[x][y][3] = 1.0  # Brightness
        #print ('X ' + str(x) + ' Y ' + str(y) + ' value: ' + str(value[0]))

# HELPERS
# a random color 0 -> 192
def random_color():
    return random.randrange(0, 7) * 32

#while True:
    ## Fill each dot with a random color
    #for dot in range(dotCount):
        #dots[dot] = (random_color(), random_color(), random_color())
#
    #dots.show()
    #time.sleep(0.0)

#
# Draw a given image matrix at a given offset
#
def showImage(img, x, y):
    for x in range(len(img)):  # For each column of image
        for y in range(len(img[0])):  # For each pixel in column
            value = img[x][y]  # Read RGB pixel in image
            pixel = getPixel(x,y)
            dots[pixel] = [value[0], value[1], value[2]]
    dots.show()

def getPixel1(col, row):
    pX = col % panelWidth
    pN = math.floor((col + 1) / panelWidth)
    pixel = (panelTotal * pN) + (panelWidth * row + pX)
    return pixel

def getPixel(col, row):
    pixel = (panelHeight * col) + row
    return pixel


print("Clearing screen")
for x in range(0, dotCount):
    dots[x] = (0, 0, 0)
dots.show()

showImage(COLUMN, 0, 0)


