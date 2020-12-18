import time
import random
import board
import adafruit_dotstar as dotstar

panelCount = 4
panelWidth=8
panelHeight=8
dotCount = panelWidth * panelHeight * panelCount

dots = dotstar.DotStar(
        board.SCK, 
        board.MOSI, 
        dotCount, 
        auto_write=False,
        brightness=0.1
        )

digits = [None]
digits[0] = [
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,1,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [1,1,1,1,1]]


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

for x in range(0, dotCount):
    dots[x] = (0, 0, 0)

dots.show()
#dots[0] = (255, 255, 0)


