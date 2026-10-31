grid = [
    ["P", "R", "O", "G", "R", "A"],
    ["M", "M", "I", "N", "G", "W"],
    ["I", "T", "H", "P", "Y", "T"],
    ["H", "O", "N", "I", "S", "C"],
    ["O", "O", "L", "X", "X", "X"]
]

path = [
    (4,5), (4,4), (4,3), (4,2), (4,1), (4,0),
    (3,0), (3,1), (3,2), (3,3), (3,4), (3,5),
    (2,5), (2,4), (2,3), (2,2), (2,1), (2,0),
    (1,0), (1,1), (1,2), (1,3), (1,4), (1,5),
    (0,5), (0,4), (0,3), (0,2), (0,1), (0,0)
]

mode = input("Enter enc to encipher or dec to decipher: ")

if mode == "enc":
    ciphertext = ""
    for loc in path:
        row = loc[0]
        col = loc[1]
        ciphertext = ciphertext + grid[row][col]
        
    print("Enciphered message:", ciphertext)

elif mode == "dec":
    cipher_input = input("Enter the 30-character ciphertext: ")
    blank_grid = [
        ["", "", "", "", "", ""],
        ["", "", "", "", "", ""],
        ["", "", "", "", "", ""],
        ["", "", "", "", "", ""],
        ["", "", "", "", "", ""]
    ]
    index = 0
    for loc in path:
        row = loc[0]
        col = loc[1]
        blank_grid[row][col] = cipher_input[index]
        index = index + 1
    plaintext = ""
    for r in range(5):
        for c in range(6):
            plaintext = plaintext + blank_grid[r][c]
            
    print("Deciphered message:", plaintext)