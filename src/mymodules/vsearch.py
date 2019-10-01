def search_for_vowels(phrase: str) -> set:
    """Display any vowels found in a given word"""
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowels_in_word = vowels.intersection(set(phrase))
    return vowels_in_word


def search_for_letters(phrase: str, letters: set = set('aeiou')) -> set:
    """Display any letters found in a given phrase"""
    return letters.intersection(set(phrase))

print(search_for_vowels("bc"))
print(search_for_letters("bc"))
print(search_for_letters("bc", set("abcde")))
