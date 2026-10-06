import graphics
gfx = graphics

win = gfx.GraphWin("To click or not to click",600,600)

buttonClick = gfx.Rectangle(gfx.Point(300, 300), gfx.Point(400, 400))
buttonClick.setFill("red")
buttonClick_text = gfx.Text(gfx.Point(350, 350), "Click Me")
Clicked_text = gfx.Text(gfx.Point(100,100), "Was I clicked?")
buttonClick.draw(win)
buttonClick_text.draw(win)
Clicked_text.draw(win)

def plot():
    btn_click = win.getMouse()
    if (btn_click.getX() >= 300 and btn_click.getX() <= 400) and (btn_click.getY() >= 300 and btn_click.getY() <= 400):
        return True
    else:
        return False
    
for i in range(0,10):
    clickCheck = plot()
    if clickCheck == True:
        Clicked_text.setText("Was I clicked? Yes!")
    else:
        Clicked_text.setText("Was I clicked? No!")
