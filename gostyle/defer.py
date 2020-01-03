from functools import wraps
import inspect

def defer_inside(f):
    # @wraps(f)
    def wrapper(*args, **kargs):
        # Empty Function
        a = 6
        def defer_func():
            pass
        ret_val = f(*args, **kargs)
        defer_func() # will not run
        print("FUNC:",defer_func)
        print("FFFF:", locals()["defer_func"])
        return ret_val
    return wrapper

def defer(*args):
    print("IN")
    def defer_runner():
        for func in args:
            func()
    stack = inspect.stack()
    inspect.getargvalues(stack[ 2   ].frame).locals["defer_func"] = defer_runner
    #inspect.getargvalues(stack[layer].frame).locals[name]=val
    print(inspect.getargvalues(inspect.stack()[2].frame).locals["defer_func"])
    inspect.getargvalues(stack[2].frame).locals["a"] = 4
    print(inspect.getargvalues(stack[2].frame).locals["a"])
    print("RUNE:",defer_runner)