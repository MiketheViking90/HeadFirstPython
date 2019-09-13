from datetime import datetime

this_min = datetime.today().minute
if (this_min % 2 != 0):
    print("this min seems odd")
else:
    print("not an odd min")

from os import getcwd

dir = getcwd()
print(dir)

import sys
platform = sys.platform
print(platform)
print(sys.version)

import datetime
today = datetime.date.today()
print(today)

print(today.day)
print(today.month)
print(today.year)

iso = datetime.date.isoformat(today)
print(iso)