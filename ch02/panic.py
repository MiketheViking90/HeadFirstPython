phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

plist.pop(0)
for i in range(4):
    plist.pop()
plist.remove("'")
print(plist)
plist.extend([plist.pop(), plist.pop()])
print(plist)
plist.insert(2, plist.pop(3))
print(plist)

plist = list(phrase)
slice1 = ''.join(plist[1:3])
slice2 = plist[4] + ''.join(plist[7:5:-1])
slice1 += (slice2)
print(slice1)

paranoid_android = "Marvin"
letters = list(paranoid_android)
for c in letters:
    print('\t', c)

for c in letters[:6]:
    print('\t', c)

