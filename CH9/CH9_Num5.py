


###################
# I didn't have the slightest clue what to do.
###################



polybius_grid = [
['A','B','C','D','E'],
['F','G','H','I','J'],
['K','L','M','N','O'],
['P','Q','R','S','T'],
['U','V','W','X','Y']
]

def letterLoc(polybius_grid,seek):

    for  row in polybius_grid:
        for chr in row:
            if chr == seek:
                locTuple = (polybius_grid.index(row),row.index(chr))
                return  (f"{locTuple[0]}{locTuple[1]}")

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
        myTuple = (int(num[0]),int(num[1]))
        decrypted = f"{decrypted} {polybius_grid[myTuple[0]][myTuple[1]]}"
    return decrypted


action = input("What do you want to do? Encrypt (enc)? Decrypt (dec) ")

if action == "enc":
    message = input("Enter a message to encrypt. ").upper()
    print(encrypt(message))
elif action == "dec":
    message = input("Enter an encrypted message. ")
    print (decrypt(message))