from datetime import datetime
import time
import random

this_min = datetime.today().minute

for i in range(5):
    sleeptime = random.randint(0, 1000)
    time.sleep(sleeptime/1000)
    if (this_min % 2 != 0):
        print("this min seems odd")
    else:
        print("not an odd min")