#Q4. Call factorial function using thread.
from threading import *
import time
def factorial(num):
    no=num
    fact=1
    while no>0:
        fact=fact*no
        no=no-1
    print("Factorial of {} is {}".format(num,fact))
n=int(input("Enter the number whose factorial is to be calculated:"))
t1=Thread(target=factorial,args=(n,))
t1.start()
