import math
def calc(endsum,intr):
    payment = endsum / (((1 + intr) ** 24 - 1) / intr)
    print(payment)

def inputs():
    endsum = float(input("What is your target down payment total? "))
    interest = float(input("What is the interest rate? "))
    interest = interest / 100
    calc(endsum,interest)

print("Let's calculate your monthly deposit.")
run = input("Ready to calculate? (y/n) ")
while run == "y":
    inputs()
    run = input("Ready to calculate? (y/n) ")