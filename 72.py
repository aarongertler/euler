# Consider the fraction, n/d, where n and d are positive integers. 
# If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

# If we list the set of reduced proper fractions for d ≤ 8 
# in ascending order of size, we get:

# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 
# 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

# It can be seen that there are 21 elements in this set.

# How many elements would be contained in the set of 
# reduced proper fractions for d ≤ 1,000,000?


# We're looking for the number of pairs (n,d) where gcd(n,d) = 1
# But we have to do that without making billions of pairwise comparisons

# This means we'll need to do some kind of trick with prime numbers.
# Let's say that we're starting with x combinations.
# x = 500,000,000,000 - 1,000,000 (all pairs where d > n).
# This is the same as (999,999)(1,000,000) / 2, since there are 999,999 possible n's and 1,000,000 possible d's.

# How much can we whittle that down by?
# First, if n and d are both even, it reduces to odd/even or odd/odd. So we'd subtract (1/4)*1 trillion combinations.
# Same goes for n and d both being multiples of 3 (subtract (1/9) * 1 trillion combinations).
# And so on, for all primes.
# For example, let's take 10,007. There are x = 1,000,000 // 10,007 multiples of this number less than 1,000,000.
# And there are x*x combinations of n and d where both are multiples of 10,007.

# This should catch everything, because any two non-relatively prime numbers must have a prime multiple in common.
# But we need to make sure we don't double-remove something. 12 / 18 has two multiples of 2, but also two multiples of 3.

# That makes things harder, but we can still find a math rule that works.
# Once we eliminate all 2n/2d, how many 3n/3d are left? 3/4 of the original count (rounded down).
# 1/4 of them were actually multiples of 6 over multiples of 6. So we only eliminate 3/4 the number of 3n/3d.
# Then, of all multiples of 5, 1/4 are 10n/10d, and 1/9 are 15n/15d (but add back the 1/36 that are 30d over 30d)
# Of all multiples of 7, we lose 1/4, 1/9, 1/25, gain back 1/36, gain back 1/100, gain back 1/225...
# ...still not seeing a pattern that is as elegant as I'd like.

# For a given n, is there a good way to tell how many d's will work for it, without checking each d for its gcd count?
# n = 1, 999,999 values of d work (999,999 * 1)
# n = 2, 499,999 values of d work (all odd numbers > 1) (999,998 * 1/2)
# n = 3, 666,665 values of d work (999,997 * 2/3)
# n = 4, 499,998 values of d work (999,996 * 1/2) (all multiples of 2 fail)
# n = 5, (999,995 * 4/5)
# n = 6, (999,994 * 1/2 * 2/3)
# n = 7, (999,993 * 6/7) -> need to round this, see below
# n = 8, (999,992 * 1/2)

# Okay, this pattern should work. For each n, we factorize it, then multiply by (f-1)/f for each prime factor f
# This still might take a while, but it's doing 3 or 4 steps times a million numbers, rather than 1 trillion steps

# Let's check d = 8:

# n = 1, 7 values of d work (7 * 1)
# n = 2, 3 values work (6 * 1/2)
# n = 3, 4 values work (5 * 2/3) -> rounds up
# n = 4, 2 values work (4 * 1/2)
# n = 5, 3 values work (3 * 4/5) -> rounds up
# n = 6, 1 value works (2 * 1/2 * 2/3) -> rounds up
# n = 7, 1 value works (1 * 6/7) -> rounds up

# It looks like we always round up. Can we prove that?
# Yes, because we always start our list of working fractions at (n / n+1).
# The number of fractions we check is either a multiple of n (in which case, no rounding)
# or not a multiple of n (in which case, the last fraction we check works, because it's not n / n*x)
# For example, with n = 5 and d = 11, we'd check 6 numbers, only one would be a multiple of 5, and the last one would be 5/11
# So we'd have 5 working numbers, which is like taking (6 * 4/5) and rounding up

from math import ceil
from sympy import primefactors

# print(factorint(6))
# print(primefactors(6)) # This is the one we want, just gives us each prime factor
# print(factor(6))
# print(factor_list(6))

max_d = 12
count = max_d - 1 # Start with all n = 1 rpfs, for simplicity's sake

for n in range(2, max_d):
	d_options = max_d - n
	multiplier = 1
	factors = primefactors(n)
	for factor in factors:
		d_options *= (factor - 1) / factor
	print("For n=", n, "we get", ceil(d_options), "options")
	count += ceil(d_options)

print(count) # Works for 8, but not for 1,000,000 -> but it's very close for 1,000,000
# My guess is that something abouut Python's internal mathematical structure shut us down here --> the pattern works perfectly for smaller numbers,
# But we're adding a lot of very large rounded numbers (maybe always rounding up was wrong?)
# Sadly, this isn't the kind of code that can easily be checked, so I can't think of a way to fix things

# Hm! Actually, looking at the pattern for small numbers in the above code, I see another pattern:
# Whenever you increase d by one, you increase the number of options by the number of d's relative primes
# So going from 8 to 9, we add 6 (there are six relative primes of 9)...
# ...okay, it's clear how this is logically equivalent to the statement of the problem. But can I use that?

# If counting relative primes were quick, my solution to 69 would've been different





# Faster way to handle this: Use dynamic programming (Dreamshire's idea).
# Start with a range of 2 through 1,000,000, with each number in the range
# representing the number of fractions that could work with that number as a denominator
# Then, loop through all n from 2 to 1,000,000
# With each loop, look at each number in the range that's a multiple of n,
# subtract the value in the range // n
# So when we look at how multiples of 2 affect the number of options
# We look at d = 2 and remove 2/2, then d = 4 and remove 2/4, 4/4, and so on
# Then we look at n = 3, remove 3/3 from d = 3, 3/6 and 6/6 from d = 6
# So 15 (for example) will have all 3n/15 removed, then all 5n/15 removed
# But we only check prime values of n, because removing multiples of 2 and 4 would be redundant

# Turns out that cutting numbers actually was efficient -- I just had to only cut primes, and only look at numbers that mattered

# def P(L):
# 	phi = list(range(L+1))
# 	for n in range(2, L+1):
# 		# print("n =", n, "phi:", phi)
# 		if phi[n] == n: # Don't use a number to cut unless it's prime (since cutting with 2 and 4 would be redundant)
# 			for k in range(n, L+1, n): # For every multiple of n, remove the number of fractions that are reducible (5 gets cut by 5 // 5 because 5/5 is removed, 10 gets cut by 10 // 5 because 5/10 and 10/10 are removed...)
# 				phi[k] -= phi[k] // n
# 	return sum(phi) - 1

# print(P(1000000)) # This gives a correct answer. I wonder what was wrong with my original algorithm?

# 303963552391