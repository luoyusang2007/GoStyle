import time
from gogo import go


# If set deamonize=false, Problems will occur. Because in windows, the thread can not accept Ctrl-C keyboard interrupt.
@go.goable()
def test_thread(title:str):
    while True:
        time.sleep(1)
        print(title)





if __name__ == "__main__":
    go.test_thread("gogogogogogo;")
    go.test_thread("go2go2go2go2gogo;")
    go(test_thread)("callcall;")
    test_thread("mainmainmain;")

    

# TODO:
# Single Instance support
# Yield Support
# Multithreading Support 
