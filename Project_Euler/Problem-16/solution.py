sum = 0
for n in str(2**1000):
	sum += int(n)
print(sum)

####
sum(map(int,str(2**1000)))

