import os
import platform
if platform.system()=='Windows': command='cls'
else: command='clear'
def clear(func):
        def wrapper(*args, **kwargs):
            os.system(command)
            return func(*args, **kwargs)
        return wrapper
def classClear(cls):
    for name, method in cls.__dict__.items():
        if callable(method) and not name=='save':
            setattr(cls, name, clear(method))
    return cls
