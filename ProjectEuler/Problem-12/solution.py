def triang(n):
    lst=list(range(1,n+1))
    return sum(lst)

from sympy import proper_divisor_count
n=8
while proper_divisor_count(triang(n)) < 500:
    n+=1
#this outputs n=12375

print(triang(12375)) 
