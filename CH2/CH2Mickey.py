def conversion(ipt):
    opt = ipt * 78.74
    return opt

userIpt = float(input("How many CM shall we translate to Mickeys? (0 to exit) "))

while userIpt != 0:
        cOpt = conversion(userIpt)
        print(f"{userIpt}CM translates to {cOpt} Mickeys!")
        userIpt = float(input("How many CM shall we translate to Mickeys? (0 to exit) "))