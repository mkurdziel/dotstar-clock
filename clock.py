import time
import math
import random
import board
import adafruit_dotstar as dotstar

panelCount = 4
panelWidth = 8
panelHeight = 8
panelTotal = panelWidth * panelHeight
dotCount = panelTotal * panelCount

dots = dotstar.DotStar(
        board.SCK, 
        board.MOSI, 
        dotCount, 
        auto_write=False,
        brightness=0.1
    )


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

def getPixel(col, row):
    pX = col % panelWidth
    print('pX: ' + str(pX))
    pN = math.floor((col + 1) / panelWidth)
    print('pN: ' + str(pN))
    pixel = (panelTotal * pN) + (panelWidth * row + pX)
    return pixel

for x in range(0, dotCount):
    dots[x] = (0, 0, 0)

dots.show()
#dots[0] = (255, 255, 0)


print("2, 4, " + str(getPixel(2, 4)))
print("11, 2, " + str(getPixel(11, 2)))
