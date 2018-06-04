#Q1. Create a threading process such that it sleeps for 5 seconds and then prints out a message.
from threading import *
import time
def display():
    time.sleep(5)
    print(current_thread().getName())
t1=Thread(target=display,name='1st Thread')
t2=Thread(target=display,name='2nd Thread')
t1.start()
t2.start()
print(current_thread().getName())
