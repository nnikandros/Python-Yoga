###calculate the number of steps for the collatz sequence
def collatzstep(n):
    i=1
    while n != 1:
        if n==2:
            return i
        elif n%2 == 0 and n >2:
            n=n/2
            i+=1
        else:
            n=3*n+1
            i+=1
    return i
# find which number gives the maximum steps   
max=0
j=1
for i in range(10**6):
    if collatzstep(i) > max:
        max=collatz(i)
        j=i
print(j)


## Another way
# make a dictionary of integer: number of steps
newdictmap={k: collatzstep(k) for k in range(1,10**6) }
# sort the above dictionary by values, descening
{k: v for k, v in sorted(newdictmap.items(), key=lambda item: item[1], reverse=True)}
