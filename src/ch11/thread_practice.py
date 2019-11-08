from threading import Thread
from time import sleep


def foo():
    sleep(3)
    print("foo")

def foo1():
    sleep(5)
    print("foo1")

def foo2():
    sleep(1)
    print("foo2")

t = Thread(target=foo)
t1 = Thread(target=foo1)
t2 = Thread(target=foo2)

t.start()
t1.start()
t2.start()