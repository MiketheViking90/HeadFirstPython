first = [1,2,3,4,5]
second = first
second.append(6)
print(first)
print(second)

third = second.copy()
print(second)
print(third)
second.append(7)

fourth = list(third)
print(fourth)

msg = "Don't panic!"
letters = list(msg)
print(letters)

slice = first[1:4:2]
slice = first[::2]
print(slice)

print(letters[:10])
print(letters[3:])
print(letters[3::2])

book = "The Hitchhiker's Guide to the Galaxy"
booklist = list(book)
print(booklist)
print(booklist[:3])

print('&'.join(booklist[:4]))

reverse = booklist[::-1]
print(''.join(reverse))

alt = booklist[::2]
print(''.join(alt))