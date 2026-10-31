import math

def cyProcess(cypString, cypKwd, mode):
    lenKwd = len(cypKwd)

    if mode == "cyp":
        arrCol = []
        cypString = cypString.replace(" ", "")
        while len(cypString) > 0:
            csChunk = list(cypString[:lenKwd])
            while len(csChunk) < lenKwd:
                csChunk.append("X")
            arrCol.append(csChunk)
            cypString = cypString[lenKwd:]

        readOrder = sorted(cypKwd)
        cypOutput = ""
        for char in range(lenKwd):
            selRow = cypKwd.index(readOrder[char]) 
            for row in range(len(arrCol)):
                cypOutput = cypOutput + arrCol[row][selRow]
            cypOutput = cypOutput + " "
            
        print("Ciphertext:", cypOutput)

    elif mode == "dec":
        chunks = cypString.split()
        numRows = len(chunks)
        grid = []
        for x in range(numRows):
            rowSkeleton = []
            for y in range(lenKwd):
                rowSkeleton.append("")
            grid.append(rowSkeleton)
            
        readOrder = sorted(cypKwd)
        for char in range(lenKwd):
            selRow = cypKwd.index(readOrder[char])
            letterChunk = chunks[char]
            for row in range(numRows):
                grid[row][selRow] = letterChunk[row]
                
        decOutput = ""
        for row in range(numRows):
            for col in range(lenKwd):
                decOutput = decOutput + grid[row][col]
                
        print("Decrypted Message:", decOutput)



mode = input("cipher or decipher? input: cyp -or dec ")
while mode != "cyp" and mode != "dec":
    mode = input("cipher or decipher? input: cyp -or dec ")

if mode == "cyp":
    cypString = input("Pass in your message: ")
elif mode == "dec":
    cypString = input("Pass in string of cipher Text Ex: 'DTOPE ASDVC ADOEE' ")

cypKwd = input("Pass in your Keyword: ")
cyProcess(cypString, cypKwd, mode)