def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True
  
def primlistlessthan(n):
    lst=[]
    for i in range(2,n+1):
        if isprime(i)== True:
            lst.append(i)
    return lst

sum(primlistlessthan(2000000))

## Alternatively there is a package in sympy that makes it faster

from sympy import nextprime
up = 2000000=2*10**6
p = 2
sum = 0
while p<=up:
    sum+=p
    p=nextprime(p)
print(sum)
