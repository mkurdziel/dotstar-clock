import time
import math
import random
import board
import adafruit_dotstar as dotstar
from os import listdir
from os.path import isfile, join, splitext
from PIL import Image, ImageOps
from datetime import datetime

panelCount = 4
panelWidth = 8
panelHeight = 8
panelTotal = panelWidth * panelHeight
dotCount = panelTotal * panelCount
asciiDir = './ascii'

FILENAME = asciiDir + '/' + '48.png'
asciiDict = {}

dots = dotstar.DotStar(
        board.SCK, 
        board.MOSI, 
        dotCount, 
        auto_write=False,
        brightness=0.1
    )

def loadImage(filename):
    imageRaw = Image.open(filename).convert("RGB")
    imageInvert = ImageOps.invert(imageRaw)
    imagePixels = imageInvert.load()
    imageWidth = imageInvert.size[0]
    imageHeight = imageInvert.size[1]
    print("%dx%d pixels" % imageInvert.size)

    print("Allocating...")
    imageColumns = [0 for x in range(imageWidth)]
    for x in range(imageWidth):
        imageColumns[x] = [[0, 0, 0, 0] for _ in range(imageHeight)]

    print("Converting...")
    for x in range(imageWidth):  # For each column of image
        for y in range(imageHeight):  # For each pixel in column
            value = imagePixels[x, y]  # Read RGB pixel in image
            imageColumns[x][y][0] = value[0]  # Gamma-corrected R
            imageColumns[x][y][1] = value[1]  # Gamma-corrected G
            imageColumns[x][y][2] = value[2]  # Gamma-corrected B
            imageColumns[x][y][3] = 1.0  # Brightness
            #print ('X ' + str(x) + ' Y ' + str(y) + ' value: ' + str(value[0]))
    return imageColumns


asciiFiles = [f for f in listdir(asciiDir) if isfile(join(asciiDir, f))]

for asciiFile in asciiFiles:
    parts = splitext(asciiFile)
    print('Loading ASCII #' + parts[0])
    asciiDict[parts[0]] = loadImage(asciiDir + '/' + asciiFile)


# a random color 0 -> 192
def random_color():
    return random.randrange(0, 7) * 32
#
# Draw a given image matrix at a given offset
#
def showImage(img, xOffset, yOffset):
    for x in range(len(img)):  # For each column of image
        for y in range(len(img[0])):  # For each pixel in column
            b = 0.1
            value = img[x][y]  # Read RGB pixel in image
            pixel = getPixel(xOffset + x,yOffset + y)
            dots[pixel] = [int(value[0] * b), int(value[1] * b), int(value[2] * b)]
    return xOffset + len(img)

def showText(text, xOffset, yOffset):
    x = xOffset
    for char in text:
        asciiNum = ord(char)
        asciiImage = asciiDict[str(asciiNum)]
        x = showImage(asciiImage, x, yOffset) + 1

def getPixel(col, row):
    pixel = (panelHeight * col) + row
    return pixel


def clearScreen():
    for x in range(0, dotCount):
        dots[x] = (0, 0, 0)

while True:
    clearScreen()
    now = datetime.now()

    currentTime = now.strftime("%-I:%M")
    showText(currentTime, 0, 0)
    dots.show()
    time.sleep(1.0)

