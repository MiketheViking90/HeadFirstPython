from typing import List


def get_evens(data: List[int]):
    return [n for n in data if n % 2 == 0]
data = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
evens = get_evens(data)
print(evens)

data = [ 1, 'one', 2, 'two', 3, 'three', 4, 'four' ]
def get_strs(data):
    return [word for word in data if isinstance(word, str)]
words = get_strs(data)
print(words)

data = list('So long and thanks for all the fish'.split())
def get_title_case(data):
    return [word.title() for word in data]
titles = get_title_case(data)
print(titles)