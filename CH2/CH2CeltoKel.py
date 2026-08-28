def conversion(ipt):
    opt = ipt + 273.15
    return opt

userIpt = float(input("How many degrees Celcius are we converting to Kelvin?"))
cont = "y"

while cont == "y":
        cOpt = conversion(userIpt)
        print(f"{userIpt} Celcius is equal to {cOpt} Kelvin!")
        cont = input("Enter y to continue. Continue? ")
        if (cont == "y"):
            userIpt = float(input("How many degrees Celcius are we converting to Kelvin?"))