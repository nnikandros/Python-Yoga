sum = 0
for n in str(2**1000):
	sum += int(n)
print(sum)

####
sum(map(int,str(2**1000)))




#### Solution 3

num = 2**1000
num_list = [int(n) for n in str(num)]
print(sum(num_list))
