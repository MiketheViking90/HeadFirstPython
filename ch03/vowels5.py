vowels = {'a', 'e', 'i', 'o', 'u'}
word = "iefnie"
found = []

for c in word:
    if c in vowels and c not in found:
        found.append(c)
print(found)

vowels = set('aeiou')
word = 'hello'

union = vowels.intersection(set(word))
print(union)

diff = vowels.difference(set(word))
print(diff)

vowels = ['a', 'e', 'i', 'o', 'u']
vowels_tuple = ('a', 'e', 'i', 'o', 'u')
print(vowels)
print(vowels_tuple)