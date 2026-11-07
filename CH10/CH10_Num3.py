import pathlib
pl = pathlib

def optGraph(dictChars: dict):
    dictHighest = max(dictChars)
    dictLowest = min(dictChars)
    print(f"{dictHighest} {dictChars[dictHighest]}")
    print("Characters measured by occurrence:")
    print(f"       0   25   50   75   100   125   150   175   200   225   250   275   300   325+")
    print("       :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    for dictEntry, count in dictChars.items():
        tick =  round(count / 4.55,None)
        line = f"{dictEntry}     : "
        if tick > 79:
            tick = 79
        for t in range(tick):
            line += "|"
        print(f"{line} {count}")


def iptFile(fileNm: pl.Path):
    content = list(fileNm.read_text(encoding="utf-8"))
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
    optGraph(dictChars)



fileNm = pl.Path(input("What is the path to your file?"))

if fileNm.exists() and fileNm.is_file():
    iptFile(fileNm)