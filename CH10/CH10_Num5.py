import graphics
import urllib.request
gfx = graphics

def ltrGraph(dictChars: dict):
    max_count = max(dictChars.values())
    winBuff = len(dictChars) * 25
    winWidth = 800
    winHeight = 400 + winBuff
    win = gfx.GraphWin("Problem 5", winWidth, winHeight)
    graphXstart = 100
    graphXend = winWidth - 100
    graphWidth = graphXend - graphXstart
    axisY = 40
    
    step_value = max_count / 9 
    
    for i in range(10):
        tickVal = int(step_value * i)
        x_pos = graphXstart + (i * (graphWidth / 9))
        gfx.Text(gfx.Point(x_pos, axisY), f"{tickVal}").draw(win)
    
    baseY = 80
    for dictEntry, count in sorted(dictChars.items()):
        gfx.Text(gfx.Point(40, baseY + 10), f"{dictEntry}").draw(win)
        bar_length = graphXstart + ((count / max_count) * graphWidth)
        pointA = gfx.Point(graphXstart, baseY)
        pointB = gfx.Point(bar_length, baseY + 20)
        rect = gfx.Rectangle(pointA, pointB)
        rect.setFill("black")
        rect.draw(win)
        gfx.Text(gfx.Point(bar_length + 30, baseY + 10), f"{count}").draw(win)
        baseY += 30
        
    win.getMouse()


url = "https://gutenberg.org/cache/epub/100/pg100.txt"
with urllib.request.urlopen(url) as response:

    text = response.read().decode('utf-8')
    content = list(text)
    content.remove(" ")
    dictChars = {
    }
    for char in range(len(content)):
        charUpper = content[char].upper()
        if charUpper == " " or charUpper.isalpha() == False:
            continue
        elif dictChars.__contains__(charUpper):
            dictChars[charUpper] += 1
        else:
            dictChars[charUpper] = 1
    #print(dictChars)
    outputFile = input("Name your file for output: ")
    if outputFile != "":
        with open(f"{outputFile}.txt", "w") as opt:
            print(f":::Letter Data:::",file=opt)
            for dictEntry, count in sorted(dictChars.items()):
                print(f"{dictEntry} : {count}",file=opt)
    ltrGraph(dictChars)
