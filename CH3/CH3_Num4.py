import math
def calc(cost,term,intr):
    payment = cost / ((1 - (1 + intr / 12) ** (-term * 12)) / (intr / 12))
    print(payment)

def inputs():
    totalCost = float(input("What is the amount being financed? "))
    term = float(input("What is the term of the loan? (Between 15 and 30) "))
    while term < 15 or term > 30:
        print("Try again. Pick a term between 15 and 30.")
        term = float(input("What is the term of the loan? "))
    interest = float(input("What is the interest rate? (compounded monthly) "))
    interest = interest / 100
    calc(totalCost,term,interest)

print("Let's calculate your monthly house payment.")
run = input("Ready to calculate? (y/n) ")
while run == "y":
    inputs()
    run = input("Ready to calculate? (y/n) ")