import time
from gostyle import go, Chan
chan1 = Chan()
def test_thread(title:str):
    for cnt in range(10):
        chan1<=cnt
        time.sleep(1)
        print(title)
def chan_reader():
    while True :
        print(chan1())
# Start the thread 
go(test_thread)("Call")
chan_reader()