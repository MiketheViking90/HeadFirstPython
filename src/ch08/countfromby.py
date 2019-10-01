class CountFromBy:

    def __init__(self, val : int = 0, incr : int = 1) -> None:
        self.val = val
        self.incr = incr

    def increase(self) -> None:
        self.val += self.incr

    def __str__(self) -> str:
        return "{}, {}".format(self.val, self.incr)


a = CountFromBy(incr = 20)
b = CountFromBy(val = 100)

a.increase()
a.increase()

print(a)
print(b)