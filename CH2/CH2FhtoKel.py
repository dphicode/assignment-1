def conversion(ipt):
    opt = (ipt - 32) * (5 / 9) + 273.15
    return opt

userIpt = float(input("How many degrees Fahrenheit are we converting to Kelvin?"))
cont = "y"

while cont == "y":
        cOpt = conversion(userIpt)
        print(f"{userIpt} Fahrenheit is equal to {cOpt} Kelvin!")
        cont = input("Enter y to continue. Continue? ")
        if (cont == "y"):
            userIpt = float(input("How many degrees Fahrenheit are we converting to Kelvin?"))