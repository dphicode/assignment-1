import math
def calc(cost,term,intr,fNm):
    with open(f"{fNm}.txt", "w") as opt:
        payment = cost / ((1 - (1 + intr / 12) ** (-term * 12)) / (intr / 12))
        print("==========================================================================================", file=opt)
        print("AMORTIZATION REPORT", file=opt)
        print(f"Principal (P0): ${cost} | Annual Rate (r): {intr * 100}% | Compounding/Year (k): 12 | Years (N): {term} Periodic Payment Amount: ${payment}", file=opt)
        print("==========================================================================================", file=opt)
        print("Payment #    Payment Amt      Interest Part      Principal Part     Remaining Principal", file=opt)
        print("------------------------------------------------------------------------------------------", file=opt)
        currentBalance = cost
        for i in range(term * 12):
            interestCharge = currentBalance * (intr / 12)
            principalPmt = payment - interestCharge
            remainingBalance = currentBalance - principalPmt
            print(f"{i + 1}             ${round(payment,2)}             ${round(interestCharge,2)}              ${round(principalPmt,2)}               ${round(remainingBalance,2)}", file=opt)
            currentBalance = remainingBalance

def inputs():
    fileNm = input("Give your file a name: ")
    totalCost = float(input("What is the amount being financed? "))
    term = int(input("What is the term of the loan? (Between 15 and 30) "))
    while term < 15 or term > 30:
        print("Try again. Pick a term between 15 and 30.")
        term = int(input("What is the term of the loan? "))
    interest = float(input("What is the interest rate? (compounded monthly) "))
    interest = interest / 100
    calc(totalCost,term,interest,fileNm)

print("Let's calculate your monthly house payment.")
run = input("Ready to calculate? (y/n) ")
while run == "y":
    inputs()
    run = input("Ready to calculate? (y/n) ")

