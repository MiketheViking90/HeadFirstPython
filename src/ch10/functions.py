def apply(fn: object, val: object) -> object:
    return fn(val)

def outer():
    def inner():
        print('inner invoked')

    print('outer invoked, return inner()')
    return inner

def myfunc(*args):
    for arg in args:
        print(arg, end=' ')
    if args:
        print()

def myfunc2(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep='->', end=' ')
    if kwargs:
        print()

def myfunc3(*args, **kwargs):
    if args:
        for arg in args:
            print(arg, end=' ')
        print()
    if kwargs:
        for k, v in kwargs.items():
            print(k, v, sep='->', end=' ')
        print()

apply(print, "hello!")
print(apply(id, "hello!"))
print(apply(type, "hello!"))

outer()

myfunc(1,2,3,4)

vals = (1,2,3,4,5)
myfunc(vals)
myfunc(*vals)

myfunc2(a='1', b='2')
dict = {
    'a': 1,
    'b': 12,
    'x': 34
}
myfunc2(**dict)
myfunc3(*vals, **dict)
