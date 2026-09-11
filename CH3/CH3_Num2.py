import math
def calc(depo,intr):
    result = depo * ((1 + intr / 12) ** 24 - 1) / (intr / 12)
    print(result)

def inputs():
    deposit = float(input("How much will you deposit monthly? "))
    interest = float(input("What is the interest rate? "))
    interest = interest / 100
    calc(deposit,interest)

print("Let's calculate your savings over 2 years")
run = input("Ready to calculate? (y/n) ")
while run == "y":
    inputs()
    run = input("Ready to calculate? (y/n) ")