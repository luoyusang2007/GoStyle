# GoStyle
Go syntax implementation in python. 

# Threading Wrapper Like goRoutine
In Golang, we can create parallel tasks via keyword `go`:
```go
//Golang
//...
go XXXX(arg1,arg2)
//...
```
In golang, the thread creating has following features:
* The parameter passing is the same as the original function defined by user.
* The original function is still usable as defined.

However, in pyton creating a thread is stupid:
```python
#Ptrhon
#...
t = threading.Thread(target=XXX, args=(arg1,arg2))
t.start()
#...
```

## How To Use in Python
If the function is self-defined, you can use decorator `@gostyle.startable()` like following:
```python
import gostyle
@gostyle.startable()
def test_thread(title:str):
    while True:
        time.sleep(1)
        print(title)
# Start the thread 
test_thread.start("Start")
# Note that the expression "test_thread('Normal')" can still run the original function in main thread.
```

Or, if the function is not a class/object method:
```python
import gostyle
@gostyle.destination()
def test_thread(title:str):
    while True:
        time.sleep(1)
        print(title)
# Start the thread 
gostyle.to.test_thread("Go To Destination")
# Note that the expression "test_thread('Normal')" can still run the original function in main thread.
```

Or:

```python
from gostyle import go
@go.goable()
def test_thread(title:str):
    while True:
        time.sleep(1)
        print(title)
# Start the thread 
    go.test_thread("Go")
# Note that the expression "test_thread('Normal')" can still run the original function in main thread.
```

If the function is not self-defined(you can not add decorator to the function), or the function is a method of a class/object(the function you defined is hard to attach to "go"(same as "to") object in this package), you can use syntax like following:
```python
from gostyle import go
def test_thread(title:str):
    while True:
        time.sleep(1)
        print(title)
# Start the thread 
go(test_thread)("Call")
```

## Run-Forever and Daemonize
The `daemon` parameter controls the deamon option in package `threading`. and the forever parameter lets you get rid of a `while True:` expression in the function you defined.
```python
from gostyle import go
def test_thread(title:str):
    # No Internal WHILE Here.
    time.sleep(1)
    print(title)
# Start the thread 
go(test_thread, forever=True)("Call Forever")
```

```python
from gostyle import go
@gostyle.startable(forever=True)
def test_thread(title:str):
    # No Internal WHILE Here.
    time.sleep(1)
    print(title)
# Start the thread 
test_thread.start("Start Loop")
```

# Defer
In Golang, defer is used to do things(usually cleaning-up) after a function returns.
## How To Use in Python
Usage of decorator `defer_inside`:
```python
from gostyle import defer_inside, defer
@defer_inside
def great_func():
    a = [1,2,3]
    b = 8
    defer(
        lambda : a.append(7),
        lambda : print(a),
        lambda : print(b)
    )
    a.append(9)
    return a,b
print(great_func())

```



-----------------------------------------
# Todos
## Threading
Manage Threads started by gostyle
Collect return values
Single Instance support
Yield Support
Multithreading Support 

## Defer
Multi-times Defer Support

## Queue
Queue Wrapper