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

import time
timefmt = time.strftime("%H:%M")
print(timefmt)
print(time.strftime("%A %p"))