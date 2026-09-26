def calcPmt(P0,r,k,N):
    r = r / 100
    d = (1 - (1 + r / k) ** (-N * k)) / (r / k)
    payment = P0 / d
    return(f"{payment:.2f}")

P0 = float(input("How much do you wish to finance? "))
r = float(input("What is the annual interest rate? "))
k = int(input("How many times is interest compounded in 1 calendar year? "))
N = int(input("How many years are we financing for? "))


print(f"Your payment: {calcPmt(P0,r,k,N)}")