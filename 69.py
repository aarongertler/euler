# Euler's Totient function, φ(n) [sometimes called the phi function],
# is used to determine the number of numbers less than n which are relatively prime to n. 

# For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

# It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

# Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.


# Two numbers are relatively prime if they have a GCF of 1
# There are a few ways we could easily check this:

# 1. Develop a "relatively prime" check that ensures no single n divides both a and b (very slow, if we have to run it on every pair of numbers)
	# This is a good algorithm to start with if we take this route: 
# 2. Get a list of non-1 factors for all numbers under 1,000,000, then check whether len(factors(a)) + len(factors(b)) == len(factors(a) + factors(b))
	# This isn't as slow (or is it?), but still makes a lot of pairwise comparisons. Can we avoid those?
		# I can't see a way to do that. No way to tell whether 999999 is relatively prime with 1000000 unless you check both...

# from math import sqrt, ceil
# from collections import defaultdict 

# # factors = defaultdict(set) 
# primes = defaultdict(list)

# def prime_factors(n):
# 	placeholder = n
# 	for i in range(2, ceil(n/2)):
# 		while placeholder % i == 0:
# 			factors[n].add(i)
# 			placeholder = placeholder / i

# for n in range(1, 10001):
# 	prime_factors(n) # Separating this out into a function might slow us down a bit?

# Unfortunately, this is already taking more than a second with just 10,000 numbers, let alone a million
# I could certainly try to build a more efficient version, but that might be a bit reinvent-the-wheel.
# Or maybe there's a factor module I can borrow from somewhere?

# max_dividend = 0
# max_n = 0 # The n that corresponds to our highest dividend
# end = 201 # Variable to test different upper limits of n

# from sympy import factorint, gcd

# # for n in range(1, 1000001):
# # 	factors = factorint(n) # This is a bit faster (15s), but still slow enough that trying a pre-built gcd function seems better

# for n in range(2, end):
# 	for p in range(1, n): # We are counting 1 here
# 		if gcd(n,p) == 1:
# 			primes[n].append(p)

# for n in range(2, end):
# 	div = n / len(primes[n])
# 	if div > max_dividend:
# 		max_dividend = div
# 		max_n = n

# print("Maximum dividend:", max_dividend, "for n=", max_n)

# Let's stop thinking about GCDs for a second, and just think about the problem.
# If we were "creating" a perfect number (one that is relatively prime with as few numbers as possible for its size), what would we do?
# It should definitely be a multiple of 2, to avoid relative primeness with all even numbers.
# But it doesn't need to be a multiple of 4, because all multiples of 4 are multiples of 2.
# So 2x avoids the same relative primes as 4x. For similar reasons, we never want to multiple n by the same number twice
# On the other hand, 6x also avoids all multiples of 3, 6, 9...
# And so it seems like the best pattern would be 2 * 3 * 5 * 7...
# This fits with initial results (that 6 is best from 1-10, and 30 from 1-100)

from sympy import primerange

primes = list(primerange(1,1000000))
n = 1
prime_count = 0

for prime in primes:
	if n * prime > 1000000:
		print("The best number is", n, 
			"and the dividend is", n / len(list(primerange(1, n))))
		break
	n *= prime

# Solves in a few seconds, would be faster if I didn't add the dividend




