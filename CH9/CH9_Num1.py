import time
import math
import threading

balls = []

#Store the relevant information about the balls in a list.
ballData = []

def bounce(drpMtr,num):
        while drpMtr > 1:
                drpMtr = round(drpMtr * .6,2)
                time.sleep(math.sqrt((2 * drpMtr) / 9.81))
                prIpt = f"ball {num} ballbounce! {drpMtr} meters"    
                ballData.append(prIpt) #Store the relevant information about the balls in a list.
                print(prIpt)

for i in range(3):
    drpMtr = float(input(f"What is the drop height of ball {i + 1} (Meters)?"))
    balls.append(drpMtr)
for i in range(len(balls)):
    thread = threading.Thread(target=bounce, args=(balls[i], i + 1))
    thread.start()