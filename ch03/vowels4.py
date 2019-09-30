def is_vowel(c):
    return c in {'a', 'e', 'i', 'o', 'u'}


word = "hitchiker's"

freq = {}
for c in word:
    if is_vowel(c):
        cnt = freq.get(c, 0)
        freq[c]  = cnt + 1

print(freq)
for k, v in sorted(freq.items()):
    print(k, v)
