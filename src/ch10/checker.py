from functools import wraps

from flask import session

def check_login(fn: object):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if 'login' in session:
            return fn(*args, **kwargs)
    return wrapper