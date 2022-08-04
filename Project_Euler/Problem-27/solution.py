from itertools import *
import numpy as np
import sympy as sp
from operator import itemgetter

a= np.array(range(-1000,1000))
b= np.array(range(-1001,1001))

#make the cartesian product into an iterator
cartesian=product(a,b)
#unpack the iterator into a list of lists 
cartesianlist=[*map(list,cartesian)]


def myquad(n, i, j):
    return n**2 + i*n + j
  
def maxn(lst) :
    n=0
    raise_flag=True
    while raise_flag :
        raise_flag=sp.isprime( myquad(n, lst[0], lst[1] ))
        if raise_flag :
            n+=1
        else :
            return n-1, lst[0], lst[1]  
          
listofmaxima=[*map(maxn,cartesianlist)]
# sort the list of maxima with descending maxima
sorted(listofmaxima,key=itemgetter(0),reverse=True)

anmax=sorted(listofmaxima,key=itemgetter(0),reverse=True)[0][1] 
bnmax=sorted(listofmaxima,key=itemgetter(0),reverse=True)[0][2] 
nmax= sorted(listofmaxima,key=itemgetter(0),reverse=True)[0][0] 
prod= anmax* bnmax
 

print(f"The product of coefficients for the quadratic expression that produces the maximum number of primes is {prod}. The cofficients are {anmax} and {bnmax}. Lastly the maximum for n is {nmax} ")
          
