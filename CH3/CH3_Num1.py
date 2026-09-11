import math
def calc(ivst, yrs, rte):
    print(ivst * math.exp(rte * yrs))

def inputs():
    investment = float(input("What is your investment amount? "))
    years = int(input("How many years? "))
    rate = float(input("What is the interest rate? "))
    rate = rate / 100
    calc(investment,years,rate)

run = input("Ready to calculate? (y/n) ")
while run == "y":
    inputs()
    run = input("Ready to calculate? (y/n) ")