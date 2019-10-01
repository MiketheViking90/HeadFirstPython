from src.ch05.vsearch import search_for_letters

search_for_letters("djfieifjef", set("aeiou"))


def test(v):
    v = v+5


def test_dict(dict):
    dict['a'] = 12

a = 7
test(a)
print(a)

d = { 'b' : 15 }
test_dict(d)
print(d)