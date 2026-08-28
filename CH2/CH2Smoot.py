def conversion(ipt):
    opt = ipt * 587.6
    return opt

userIpt = float(input("How many KM shall we translate to Smoots? (0 to exit) "))

while userIpt != 0:
        cOpt = conversion(userIpt)
        print(f"{userIpt}KM translates to {cOpt} Smoots!")
        userIpt = float(input("How many KM shall we translate to Smoots? (0 to exit) "))