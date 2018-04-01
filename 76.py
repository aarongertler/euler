# It is possible to write five as a sum in exactly six different ways:

# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1

# How many different ways can one hundred be written as a sum 
# of at least two positive integers?

# ... this is exactly #78 (which I did first), but subtracting one from every sum

from math import ceil

def pent(k): # Formula for calculating *generalized* pentagonal numbers
	if k < 1: return 0
	if k % 2 == 0:
		k = -1 * (k/2)
	else:
		k = ceil(k/2)
	return (k * (3*k - 1)) / 2

# for i in range(1,8):
# 	print(pent(i))

cached_partitions = [1] # We only ever want to have to find each partition once

def partitions(n):
	# print("Checking partitions for", n)
	answer = 0
	count = 1
	if n < 0: return 0
	# if n < len(cached_partitions): return cached_partitions[int(n)]
	while n >= pent(count): # This recursion took a while to debug; turns out that I wasn't iterating the count correctly
		# print("Count:", count, "n:", n)
		index = int(n - pent(count))
		if (count % 4 == 1) or (count % 4 == 2):
			answer += cached_partitions[index]
		if (count % 4 == 3) or (count % 4 == 0):
			answer -= cached_partitions[index]
		count += 1
	return answer


for i in range(1, 101):
	p = partitions(i)
	cached_partitions.append(p)

print(cached_partitions[100] - 1)