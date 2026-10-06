def primeness(myNum):
    found = False
    if myNum <= 1:
        return False
    for i in range(2,myNum):
        divResult = myNum % i
        if divResult == 0:
            return False
    return True

myNum = int(input("Give me a number, let's check for primeness."))
isPrime = primeness(myNum)
if isPrime == False:
    print(f"{myNum} is not prime.")
else:
    print(f"{myNum} is prime.")
