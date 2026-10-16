import time
import math
import graphics
gfx = graphics

win = gfx.GraphWin("Bouncy Ball Bonanza",600,600)
win.setCoords(0, 0, 600, 600)
def bounce(drpMtr):
    if drpMtr > 610:
        drpMtr = 610
    print(drpMtr)
    mid = win.getWidth() / 2
    point = gfx.Point(mid,drpMtr)
    ball = gfx.Circle(point,25)
    ball.setFill("red")
    ball.draw(win)
    fallRange = drpMtr - 13
    while drpMtr > 10:
        for meter in range(fallRange):
          ball.move(0,-1)
          time.sleep(((math.sqrt((2 * drpMtr) / 9.81)) / fallRange) / 5)
        drpMtr = round(drpMtr * .6,None)
        fallRange = drpMtr
        for meter in range(fallRange):
            ball.move(0,1)
            time.sleep(((math.sqrt((2 * drpMtr) / 9.81)) / fallRange) / 5)

    win.getMouse()

drpMtr = int(input("What is the drop height (Meters)?"))
bounce(drpMtr)