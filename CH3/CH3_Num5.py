import math
def calc(payment,intr):
    #payment = cost / ((1 - (1 + intr / 12) ** (-term * 12)) / (intr / 12))
    term = 15
    for i in range(2):
        cost = payment * ((1 - (1 + intr / 12) ** (-term * 12)) / (intr / 12))
        print(f"{term} loan term will afford a house of {cost}")
        term = 30

def inputs():
    payment = float(input("What is your monthly payment? "))
    interest = float(input("What is the interest rate? (compounded monthly) "))
    interest = interest / 100
    calc(payment,interest)

print("Let's calculate how much you can afford to finance.")
run = input("Ready to calculate? (y/n) ")
while run == "y":
    inputs()
    run = input("Ready to calculate? (y/n) ")