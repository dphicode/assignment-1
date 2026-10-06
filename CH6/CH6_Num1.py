def chaos(k,x,n):
    for i in range(1,n + 1):
        x = k * x * (1 - x)
        print(f"Iteration {i}: {x}")
input

k = float(input("Provide K (float): "))
x = float(input("Provide X (float): "))
if x < 0 or x > 1: #modified code
    raise SystemExit("Invalid. x must be between 0 and 1.")
else: #modified code
    n = int(input("Provide N (int): "))
    chaos(k,x,n)