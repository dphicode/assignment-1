def conversion(ipt):
    opt = ipt / 500000
    return opt

userIpt = float(input("How many followers shall we translate to Wheatons? (0 to exit) "))

while userIpt != 0:
        cOpt = conversion(userIpt)
        print(f"{userIpt} followers translates to {cOpt} Wheatons!")
        userIpt = float(input("How many followers shall we translate to Wheatons? (0 to exit) "))