def Smuckers(age):
    if age >= 100:
        print("Congtatulations for appearing on the Smucker's Jar!")
    elif age > 65 and age < 100:
        print("You're a senior citizen.")
    elif age >= 20 and age <= 65:
        print("You're an adult.")
    elif age >= 13 and age <= 19:
        print("You're a teenager.")
    elif age >= 0 and age <= 12:
        print("You're a child.")
    else:
        print("You're impossible!")

userAge = int(input("What's your age? "))
Smuckers(userAge)
