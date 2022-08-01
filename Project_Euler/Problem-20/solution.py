mult = 1
for i in range(1,101):
    mult*= i
 
sum=0
for n in str(mult):
    sum += int(n)
print(sum)
