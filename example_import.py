import time
#from gopy import go, startable
import gogo



@gopy.destination()
@gopy.startable()
def test_thread(title:str):
    while True:
        time.sleep(1)
        print(title)


# If set deamonize=false, Problems will occur. Because in windows, the thread can not accept Ctrl-C keyboard interrupt.
@gopy.startable(deamon = False,forever=True)
def test_thread_no_loop(title:str):
    time.sleep(1)
    print(title)


if __name__ == "__main__":
    gopy.to.test_thread("gogogogogogo;")
    test_thread.start("start1start1;")
    # test_thread_no_loop.start("start2start2")
    test_thread("mainmainmain;")

    

# TODO:
# Single Instance support
# Yield Support
# Multithreading Support 
