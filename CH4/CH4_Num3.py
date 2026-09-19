import math
import graphics
import random
gfx = graphics

def myRanNum():
    randomNum = random.uniform(.1,1)
    return randomNum

win = gfx.GraphWin("Problem 3",600,600)
win.setCoords(0, -8, 100, 8)
newY = win.height / 2

for x in range(0,100):
    myRand = myRanNum()
    newY = 3.9 * myRand * (1 - myRand)
    newPoint = gfx.Point(x,newY)
    gfx.Point.draw(newPoint,win)

win.getMouse()
win.close()