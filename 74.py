# The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

# 1! + 4! + 5! = 1 + 24 + 120 = 145

# Perhaps less well known is 169, in that it produces the longest chain of numbers 
# that link back to 169; it turns out that there are only three such loops that exist:

# 169 → 363601 → 1454 → 169
# 871 → 45361 → 871
# 872 → 45362 → 872

# It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

# 69 → 363600 → 1454 → 169 → 363601 (→ 1454)
# 78 → 45360 → 871 → 45361 (→ 871)
# 540 → 145 (→ 145)

# Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

# How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?


# Looks like brute force time?

# def factorial(n):
# 	if n == 0: return 1
# 	result = 1
# 	while n > 1:
# 		result *= n
# 		n -= 1
# 	return result

# Found a shorter function (though it's not faster):

# from functools import reduce

# def factorial(n): return reduce(lambda x,y:x*y,range(1,n+1),1)

# But actually, just listing the factorials ought to be much faster... (yes, cuts time by 2/3)

factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

# print(factorial(5))

def factorial_sum(n):
	result = 0
	div = 10
	while n > 0:
		digit = n % div
		# result += factorial(digit)
		result += factorials[digit]
		n = n // div
	return result

# print(factorial_sum(124))

def factorial_chain(n):
	terms = []
	while n not in terms:
		terms.append(n)
		n = factorial_sum(n)
	return len(terms)

# print(factorial_chain(540))

count = 0
limit = 1000000

for n in range(1, limit + 1):
	if n % 10000 == 0: print("n =", n)
	if factorial_chain(n) == 60:
		print("Found one!")
		count += 1

print(count) # Takes almost exactly a minute to run, comes out clean and corrects

# Ways to make this faster:
# When a chain ends on a certain number, learn to halt the moment you spot that number in a future number's chain? Don't think that would work.
# (But perhaps you could save time on a few basic patterns, like the 169 pattern

# Looks like Dreamshire did something similar, analyzing solutions they found and noticing which sets of digits led to 60-length chains 
# (since any permutation of a successful 60-chain number will also be a 60-chain number)

# https://blog.dreamshire.com/project-euler-74-solution/