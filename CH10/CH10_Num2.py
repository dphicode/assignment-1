import pathlib
pl = pathlib

#store the Polybius checkerboard in a list of lists.
#(no change from my old homework)
polybius_grid = [
['A','B','C','D','E'],
['F','G','H','I','J'],
['K','L','M','N','O'],
['P','Q','R','S','T'],
['U','V','W','X','Y']
]

################################
###README README README README##
################################
#Assignment called for Ch9 - 3
#This is Ch 9 - 2; 9 - 3 did not
#use tuples like ths problem
#suggested. 


def letterLoc(polybius_grid,seek):

    for  row in polybius_grid:
        for chr in row:
            if chr == seek:
                #Tuple requested in homework
                locTuple = (polybius_grid.index(row),row.index(chr))
                return  (f"{locTuple[0]}{locTuple[1]}")
                #return  (f"{polybius_grid.index(row)}{row.index(chr)}")

def encrypt(message):
    encrypted = ""
    for char in message:
        print(char)
        encrypted = f"{encrypted} {letterLoc(polybius_grid,char)}"
    return encrypted

def decrypt(message):
    decrypted = ""
    msg = message.split()
    for num in msg:
        #Tuple requested in homework
        myTuple = (int(num[0]),int(num[1]))
        decrypted = f"{decrypted} {polybius_grid[myTuple[0]][myTuple[1]]}"
        #decrypted = f"{decrypted} {polybius_grid[int(num[0])][int(num[1])]}"
    return decrypted


action = input("What do you want to do? Find letter (find)? Encrypt (enc)? Decrypt (dec) ")

if action == "find":
    myChar = input("Enter a letter to find: (Enter more than one, we use the first) ")
    myChar = myChar[0].upper()
    print(letterLoc(polybius_grid,myChar))
elif action == "enc":
    message = input("Enter a message to encrypt. ").upper()
    print(encrypt(message))
elif action == "dec":
    fileNm = pl.Path(f"CH10_Num2_Tuples.txt")
    content = fileNm.read_text(encoding="utf-8")
    print (decrypt(content))
else:
    print("You broke it. try again.")