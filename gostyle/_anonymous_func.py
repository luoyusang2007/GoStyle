import inspect

def af_set_var(name,val, layer = 2):
    stack = inspect.stack()
    inspect.getargvalues(stack[layer].frame).locals[name]=val

def af_get_var(name, layer = 2):
    stack = inspect.stack()
    return inspect.getargvalues(stack[layer].frame).locals[name]
    
def func(*args):
    def _():
        for func_ in args:
            func_()
    return _
