import math
import graphics
#import random
gfx = graphics

#def myRanNum():
#    randomNum = random.uniform(.1,1)
#    return randomNum

win = gfx.GraphWin("Problem 3 (mod)",600,600)
win.setCoords(0, -8, 100, 8)
newY = win.height / 2
newX = 0

iptAxisX = gfx.Entry(gfx.Point(70,7), 10)
iptAxisY = gfx.Entry(gfx.Point(70,6), 10)
buttonPlot = gfx.Rectangle(gfx.Point(60, 4), gfx.Point(70, 5))
buttonExit = gfx.Rectangle(gfx.Point(75,4), gfx.Point(85,5))
buttonPlot_text = gfx.Text(gfx.Point(65, 4.5), "Graph")
buttonExit_text = gfx.Text(gfx.Point(80,4.5), "Exit")
labelX_text = gfx.Text(gfx.Point(50,7), "X Axis")
labelY_text = gfx.Text(gfx.Point(50,6), "Y Axis")
buttonPlot.setFill("red")
buttonExit.setFill("blue")
iptAxisX.setFill("orange")
iptAxisY.setFill("green")
buttonPlot.draw(win)
buttonExit.draw(win)
iptAxisX.draw(win)
iptAxisY.draw(win)
buttonPlot_text.draw(win)
buttonExit_text.draw(win)
labelX_text.draw(win)
labelY_text.draw(win)

#Problem 5 didn't make sense to me; I know this isn't exactly what you asked for but I needed something across the finish line.
def plot():
    btn_click = win.getMouse()
    if (btn_click.getX() >= 60 and btn_click.getX() <= 70) and (btn_click.getY() >= 4 and btn_click.getY() <= 5):
        #myRand = myRanNum()
        #newY = 3.9 * myRand * (1 - myRand)
        newX = float(iptAxisX.getText())
        newY = float(iptAxisY.getText())
        newPoint = gfx.Point(newX,newY)
        gfx.Point.draw(newPoint,win)
    elif (btn_click.getX() >= 75 and btn_click.getX() <= 85) and (btn_click.getY() >= 4 and btn_click.getY() <= 5):
        win.close()
while True:
    plot()