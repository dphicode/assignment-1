def triType(sideA,sideB,sideC):
    if sideA == sideB == sideC:
        print("Your triangle is an equilateral! Yay Telly!!")
    elif sideA == sideB or sideB == sideC or sideA == sideC:
        print("This triangle is an isoseles! That's two equal sides, Telly!")
    else:
        print("Wow Telly! This triangle has no equal sides! it's called scalene.")


sideA = float(input("Enter length of the first side: "))
sideB = float(input("Enter length of the second side: "))
sideC = float(input("Enter length of the third side: "))
triType(sideA,sideB,sideC)