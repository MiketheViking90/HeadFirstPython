from datetime import datetime

this_min = datetime.today().minute

if (this_min % 2 != 0):
    print("this min seems odd")
else:
    print("not an odd min")