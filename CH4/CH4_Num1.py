import math
import graphics
gfx = graphics

def calcDrawing(sides,radius):
    angle = 360 / sides
    vertices = []
    win = gfx.GraphWin()

    middle_x = win.width / 2
    middle_y = win.height / 2
    
    for i in range(sides):
        i_angle = i * angle
        i_rad = math.radians(i_angle)
        coordX = middle_x + radius * math.cos(i_rad)
        coordY = middle_y + radius * math.sin(i_rad)
        vertices.append(gfx.Point(coordX,coordY))

    newPolygon = gfx.Polygon(vertices)
    newPolygon.draw(win)

    print("Click in window to close.")
    win.getMouse()
    win.close()

def getInput():
    sides = int(input("How many sides does your polgyon have? "))
    radius = float(input("What is the radius? "))
    calcDrawing(sides,radius)

print("Let's draw some shapes and stuff.")
getInput()


