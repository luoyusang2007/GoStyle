import inspect 

b=3
def outer_func(fun):
    a=1
    fun()
    called_function()
    print(a)


def called_function():
    stack = inspect.stack()
    print(stack)
    print("locals before change:", inspect.getargvalues(stack[2].frame))
    inspect.getargvalues(stack[1].frame).locals["a"] = 2
    inspect.getargvalues(stack[2].frame).locals["b"] = 4

outer_func(lambda: called_function())
print(b)




# func
def set_var(name,val, layer = 2):
    stack = inspect.stack()
    inspect.getargvalues(stack[layer].frame).locals[name]=val
    
def func(func_):
    ee=5
    func_()
    print(locals())


func(
    lambda : set_var("ee", 3)
)
