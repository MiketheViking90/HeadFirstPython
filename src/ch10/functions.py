def apply(fn: object, val: object) -> object:
    return fn(val)

def outer():
    def inner():
        print('inner invoked')

    print('outer invoked, return inner()')
    return inner

apply(print, "hello!")
print(apply(id, "hello!"))
print(apply(type, "hello!"))

outer()