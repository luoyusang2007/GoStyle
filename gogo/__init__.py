import threading
from functools import wraps



def _decorator_attach(deamon = True, forever = False, attached_obj=None, _name=""):
    def _decorator_body(f):
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
            target_thread.setDaemon(deamon)
            target_thread.start()

        if attached_obj:
            nonlocal _name
            if not _name:
                pass
                #_name = f.__name__ #strange!
            else:
                raise Exception("Need a Name...")
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
    def __call__(self, func, deamon = True, forever = False):
        _decorator_body =  _decorator_attach(deamon = deamon, forever = deamon)
        return _decorator_body(func)

    def goable(self, deamon = True, forever = False): # Decorator Generator
        def _decorator_body(f):
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
                target_thread.setDaemon(deamon)
                target_thread.start()
            setattr(self,f.__name__,wrapper)
            return f
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
def startable(deamon = True, forever = False): # Decorator Generator
    def _decorator_body(f):
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
            target_thread.setDaemon(deamon)
            target_thread.start()
        #setattr(f,"start",wrapper)
        f.start = wrapper
        return f
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
def destination(deamon = True, forever = False): # Decorator Generator
    def _decorator_body(f):
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
            target_thread.setDaemon(deamon)
            target_thread.start()
        setattr(to,f.__name__,wrapper)
        #_names[f.__name__] = wrapper
        return f
    return _decorator_body
