'''Q3. Make a list that has 5 elements.Create a threading process that prints the 5 elements of the list with a delay of multiple of 2 sec between each display.
Delay goes like 2sec-4sec-6sec-8sec-10sec '''
from threading import *
import time
def display(num):
    i=1
    for n in num:
        print(n)
        time.sleep(2*i)
        i=i+1
num=[6,2,3,4,1]
t1=Thread(target=display,args=(num,))
t2=Thread(target=display,args=(num,))
t1.start()
t2.start()

        
