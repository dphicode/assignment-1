
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def phi(n):
    rplist = []
    for i in range(1, n):
        if gcd(i, n) == 1:
            rplist.append(i)   
    return rplist

numIpt = int(input("Enter a number. "))
result = phi(numIpt)
output = ""
for num in result:
    output = f"{output}, {num}"
    
print(f"Numbers relatively prime for {numIpt}: {output}")
