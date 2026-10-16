import time
import math

def bounce(drpMtr):
    while drpMtr > 1:
        drpMtr = round(drpMtr * .6,2)
        time.sleep(math.sqrt((2 * drpMtr) / 9.81))
        print(f"bounce! {drpMtr} meters")


drpMtr = float(input("What is the drop height (Meters)?"))

bounce(drpMtr)