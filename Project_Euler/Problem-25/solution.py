## my first try was the following but is too slow :

import numpy as np
a=[[1,1],
   [1,0]]
Q=np.array(a)
A=np.array(a)

n=1
no_of_iter=1
while n < 10:
    Q = np.dot(Q,A)
    n = len(str(Q[0,1]))
    no_of_iter+=1
print(no_of_iter,Q[0,1] )  

##second attempt that works. Adding @cache decorator makes things faster
from functools import *
@cache
def fibb(n):
    if n in {0,1}:
        return n
    else:
        return fibb(n-1) + fibb(n-2)
      
n=0
x=1
while n < 1000:
    n = len(str(fibb(x)))
    x+=1
print(x-1) 
ind= x-1    
f"The index of the first Fibbo number that is has 1000 digits is {ind}""

## third atttemt that also works. There is a closed formula to calculate the F_n term which also makes things fast

import scipy as sp
import math

phi = sp.constants.golden
def fibboclosed(n):
    return math.floor(phi**n/ (math.sqrt(5)))

## just need to fix an overflow error :]   
  
   ## another solution from the forum 
   n = 2
prev = 1
curr = 1
while curr < 10 ** 999:
    prev, curr = curr, prev + curr
    n += 1

print(f"n = {n}")
print(f"Fibonacci number = {curr}")
  
