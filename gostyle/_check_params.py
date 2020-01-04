import datetime, time

import inspect

def check_str(func):
   def wrapper(*args, **kwargs):
       obj = inspect.signature(func)
       params = obj.parameters
       for k, v in enumerate(params.items()):
           name, param = v
           for i in args:
               if not isinstance(i, param.annotation):
                   print("{}: {} is not string".format(name, i))
                   raise TypeError
       ret = func(*args, **kwargs)
       return ret
   return wrapper

@check_str

def str_add(str1:str, str2:str):
   t1 = datetime.datetime.now()
   new_str = str1 + str2
   time.sleep(3)
   delta_time = (datetime.datetime.now() - t1).total_seconds()
   print(new_str, round(delta_time), sep="\n")
str_add(3, "4")


# From：https://www.jianshu.com/p/f59667bd321c
