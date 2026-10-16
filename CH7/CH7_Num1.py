def simpleDiv(dividend,divisor):
    iteration = 0
    while dividend >= divisor:
        dividend -= divisor
        iteration += 1
    return iteration

dividend = int(input("What is the dividend? "))
divisor = int(input("What is the divisor? "))

print(simpleDiv(dividend,divisor))