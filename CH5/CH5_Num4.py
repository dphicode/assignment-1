import graphics
import math
gfx = graphics
win = gfx.GraphWin("",600,600)

def drawNgon(nos,rad):
    angle = 360 / nos
    vertices = []
    middle_x = win.width / 2
    middle_y = win.height / 2
    for i in range(nos):
        i_angle = i * angle
        i_angle = (-90 - (180 / nos)) + i_angle
        i_rad = math.radians(i_angle)
        coordX = middle_x + rad * math.cos(i_rad)
        coordY = middle_y + rad * math.sin(i_rad)
        vertices.append(gfx.Point(coordX,coordY))
        #print(f"{i} iteration {coordX} X  and {coordY} Y")
    
    newPolygon = gfx.Polygon(vertices)
    newPolygon.draw(win)
    btnClick()

def btnClick():
    btn_click = win.getMouse()
    if (btn_click.getX() >= 390 and btn_click.getX() <= 450) and (btn_click.getY() >= 70 and btn_click.getY() <= 90):
        if buttonPlot_text.getText() == "Exit":
            win.close()
        else:
            numSides = int(iptNumSides.getText())
            radius = int(iptRadius.getText())
            buttonPlot_text.setText("Exit")
            drawNgon(numSides,radius)
    else:
        btnClick()

iptNumSides = gfx.Entry(gfx.Point(400,50), 10)
lblNumSides_text = gfx.Text(gfx.Point(280,50), "Number of Sides")
iptNumSides.setFill("white")
iptRadius = gfx.Entry(gfx.Point(400,20), 10)
lblRadius_text = gfx.Text(gfx.Point(280,20),"Radius")
iptRadius.setFill("white")
buttonPlot = gfx.Rectangle(gfx.Point(390, 70), gfx.Point(450, 90))
buttonPlot_text = gfx.Text(gfx.Point(420, 80), "Graph")
buttonPlot.setFill("red")


buttonPlot.draw(win)
iptNumSides.draw(win)
iptRadius.draw(win)
lblRadius_text.draw(win)
buttonPlot_text.draw(win)
lblNumSides_text.draw(win)
btnClick()