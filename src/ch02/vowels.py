vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels:")

word = word.lower()
print(word)

found = []
for c in word:
    if (c in vowels and c not in found):
        found.append(c)
        print(c)

print(found)