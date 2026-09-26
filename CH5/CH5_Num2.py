def kToF(k):
    while k - 20 < 300:
        if k > 300:
            k = 300
        fahrenheit = (k - 273.15) * (9 / 5) + 32
        print(f"{k} = {fahrenheit}")
        k = k + 20

iptK = float(input("Choose dagrees Kelvin to start with: "))
kToF(iptK)
