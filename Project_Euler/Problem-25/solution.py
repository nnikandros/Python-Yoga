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

## third atttemt that also works. There is a closed formula to calculate the F_n term which also makes things fast

import scipy as sp
import math

phi = sp.constants.golden
def fibboclosed(n):
    return math.floor(phi**n/ (math.sqrt(5)))
  
  
