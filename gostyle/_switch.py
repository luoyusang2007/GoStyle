from collections import OrderedDict
import inspect
def sw_set_var(name,val, layer = 3):
    stack = inspect.stack()
    inspect.getargvalues(stack[layer].frame).locals[name]=val
def _empty_func():
    pass
case = lambda _:_
class Default:
    pass
default = Default
pass_break = ()
def switch(value, cases_dict:OrderedDict):
    _default = cases_dict.get(default,_empty_func)
    func_or_tuple = cases_dict.get(value, _default)
    if callable(func_or_tuple):
        func_or_tuple()
    elif type(func_or_tuple) in [tuple,list]:
        for func in func_or_tuple:
            func()
        

