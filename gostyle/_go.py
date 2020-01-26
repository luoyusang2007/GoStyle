import threading
from functools import wraps
from queue import Queue


class Chan(Queue):
    def __init__(self,**kargs):
        super().__init__(**kargs)
    def __call__(self,val=None):
        if val:
            self.put(val)
        else:
            return self.get()
    def __neg__(self):
        return self.get()
    def __pos__(self):
        return self.get()
    def __le__(self,val):
        self.put(val)
    def __lshift__(self,val):
        self.put(val)
    def __rrshift__(self,val):
        self.put(val)
    def __iadd__(self,val):
        self.put(val)
        return self

def _decorator_attach(daemon = True, forever = False, attached_obj=None, _name=""):
    def _decorator_body(f):
        nonlocal _name
        nonlocal attached_obj
        @wraps(f)
        def wrapper(*args, **argv):
            if forever:
                @wraps(f)
                def forever_wrapper(*args, **argv):
                    while True:
                        f(*args, **argv)
                target_thread = threading.Thread(target=forever_wrapper, args=args, kwargs=argv)
            else:
                target_thread = threading.Thread(target=f, args=args, kwargs=argv)
            target_thread.setDaemon(daemon)
            target_thread.start()
        if attached_obj == "it_self":
            attached_obj = f
            setattr(attached_obj,_name,wrapper)
            return f
        elif attached_obj:
            if not _name:
                _name = f.__name__
            setattr(attached_obj,_name,wrapper)
            return f
        else:
            return wrapper
    return _decorator_body


# To Support Following Syntax:
# ====================================
# from package_go import go
# @go.goable()
# def XXXX(arg_1)
#     ...
# go.XXXX(arg_1)
# ====================================
# from package_go import go
# def XXXX(arg_1)
#     ...
# go(XXXX)(arg_1)
# ====================================
class Go:
    def __call__(self, func, daemon = True, forever = False):
        _decorator_body =  _decorator_attach(daemon = daemon, forever = daemon)
        return _decorator_body(func)

    def goable(self, daemon = True, forever = False): # Decorator Generator
        _decorator_body = _decorator_attach(daemon = daemon, forever = forever, attached_obj=self) # Attach to instance of Go
        return _decorator_body
go = Go()



# To Support Following Syntax:
# ====================================
# import package_go
# @package_go.startable()
# def XXXX(arg_1)
#     ...
# XXXX.start(arg_1)
# ====================================
def startable(daemon = True, forever = False): # Decorator Generator
    _decorator_body = _decorator_attach(daemon = daemon, forever = forever, attached_obj="it_self", _name="start") # Attach to function
    return _decorator_body


# To Support Following Syntax:
# ====================================
# import package_go
# @package_go.destination()
# def XXXX(arg_1)
#     ...
# package_go.to.XXXX(arg_1)
# ====================================
to = go 
def destination(daemon = True, forever = False): # Decorator Generator
    _decorator_body = _decorator_attach(daemon = daemon, forever = forever, attached_obj=to) # Attach to function
    return _decorator_body
