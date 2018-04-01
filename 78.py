# Let p(n) represent the number of different ways in which n coins can be separated into piles.
# For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

# OOOOO
# OOOO   O
# OOO   OO
# OOO   O   O
# OO   OO   O
# OO   O   O   O
# O   O   O   O   O

# Find the least value of n for which p(n) is divisible by one million.


# Finding the number of piles, efficiently:
# This should be recursive, I'd guess, because P(n) and P(n-1) look very similar. Let's try it out:

# 1: O (1) (1 total solution)
# 2: (OO), (O O) (2, 1+1) (2 total solutions)
# 3: (OOO), (OO O), (O O O) (3, 2+1, 1+1+1) (3)
# 4: (OOOO), (OOO O), (OO OO), (OO O O), (O O O O) (4, 3+1, 2+2, 2+1+1, 1+1+1+1) (5)
# 5: (5, 4+1, 3+1+1, 2+2+1, 2+1+1+1, 1+1+1+1+1, 3+2) (7)
# 6: (6, 5+1, 4+1+1, 3+2+1, 3+1+1+1, 2+2+1+1, 2+1+1+1+1, 1+1+1+1+1+1, 4+2, 2+2+2, 3+3) (10)
# 7: (7, 6+1, (9 other solutions from 6), 5+2, 3+2+2, 4+3) (14)
# 8: (8, 7+1, (13 other solutions from 7), 6+2, 4+2+2, 3+3+2, 5+3, 4+4) (20)
# 9: (9, 8+1, (19 other solutions from 8), 7+2, 5+2+2, 4+3+2, 6+3, 3+3+3, 5+4) (27)

# P(n) = (1 solution with one pile) + (solutions with 1 as smallest pile) + (solutions with 2 as smallest pile)... + (1 solution with floor(n/2) as smallest pile)
# P(n) = 1 + P(n-1) + ... + 1
# So what's in the middle of the above? Let's look at the pattern in another way:

# NOTE: After checking OEIS, the below sequence starts to be off at 8 -- didn't check the count carefully enough

# 1: 1 pile
# 2: 1 pile (2 smallest) + 1 pile (1 smallest)
# 3: 1 (3) + 2 (1)
# 4: 1 (4) + 3 (1) + 1 (2)
# 5: 1 (5) + 5 (1) + 1 (2)
# 6: 1 (6) + 7 (1) + 2 (2) + 1 (3)
# 7: 1 (7) + 11 (1) + 2 (2) + 1 (3)
# 8: 1 (8) + 15 (1) + 3 (2) + 1 (3) + 1 (4)
# 9: 1 (9) + 21 (1) + 3 (2) + 2 (3) + 1 (4)
# 10: 1 (10) + 28 (1) + 4 (2) + 2 (3) + 1 (4) + 1 (5) (sum: 36)

# Idea of the (ugly) algorithm below:
# If we're trying to figure out how many combinations with a smallest pile of size x are in the nth pile
# (for example, how many combinations have a smallest pile of 2 for 9),
# We look to the number of piles of x for pile n - x
# So for 9 and 2, we know that 9 can be 7+2, so we look to see how many smallest-2 piles can be made with 7.
# We find 5+2 and 3+2+2.
# So we know that 9 has three combinations: 5+2+2, 3+2+2+2, and the new 7+2.
# This pattern should hold for all piles of smallest size x in a pile of n coins.

# div_check = 1000000
# piles = [[],[1],[1,1],[1,1],[1,3,1],[1,5,1]] # Index the first few piles as a starting point
# pile = 6

# while sum(piles[-1]) % div_check != 0:
# 	piles.append([])
# 	piles[pile] = [1]
# 	piles[pile].append(sum(piles[pile - 1]))
# 	for i in range(2, int(pile / 2)):
# 		# print("Looking for smallest number", i, "piles in pile", pile - i, "which looks like:", piles[pile - i])
# 		if len(piles[pile - i]) > i:
# 			piles[pile].append(piles[pile - i][i] + 1)
# 		else:
# 			piles[pile].append(1)
# 	piles[pile].append(1)
# 	pile += 1

# print(len(piles) - 1) # First pile is "0", so subtract one

# Hm. This code brought about a memory error.

# Perhaps not saving the piles we don't need anymore will help? Is reading over a long list too much effort?
# ...but with this system, we do need to save a lot of piles from the past. I don't think removal will make too much of a difference.


# Well, I think this would work on a computer the size of the universe, but I don't have one, so it's off to Wikipedia.


# https://en.wikipedia.org/wiki/Pentagonal_number_theorem

# These are called "integer partitions". I'll trust in Euler when he gives the generating function as:
# p(n)=p(n-1)+p(n-2)-p(n-5)-p(n-7)+p(n-12)+p(n-15)-p(n-22)-... (plus, plus, minus, minus)
# The numbers attached to n are the pentagonal numbers:
# k*(3k-1)/2 for k = 1, −1, 2, −2, 3, etc.

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

i = 0
p = 1

while p % 1000000 != 0:
	i += 1
	if i % 1000 == 0: print("Checking p(n) for n =", i)
	p = partitions(i)
	cached_partitions.append(p)

print("The answer is:", i, "with partition:", p)


# Ways to make this faster: 
# Cache an array of a few hundred pentagonal numbers rather than running a function over and over again
# (Probably other ways as well, and the code could be shorter, though I like the readability here)



