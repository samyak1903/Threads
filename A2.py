#Q2. Make a thread that prints numbers from 1-10, waits for 1 sec between
from threading import *
import time
def display():
    for i in range(10):
        print(i+1)
        time.sleep(1)
t1=Thread(target=display,name='1st thread')
t2=Thread(target=display,name='2nd thread')
t1.start()
t2.start()
