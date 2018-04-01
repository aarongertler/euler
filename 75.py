# It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided
# right angle triangle in exactly one way, but there are many more examples.

# 12 cm: (3,4,5)
# 24 cm: (6,8,10)
# 30 cm: (5,12,13)
# 36 cm: (9,12,15)
# 40 cm: (8,15,17)
# 48 cm: (12,16,20)

# In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle,
# and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form
# exactly three different integer sided right angle triangles.

# 120 cm: (30,40,50), (20,48,52), (24,45,51)

# Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?


# Ideas to start with:

# 3+4+5 = 12, 5+12+13 = 30, 8+15+17 = 40 so any multiple of 12 and 30, or 12 and 40, etc., will have more than one triangle
# 2*2*3, 2*3*5, 2*2*2*5... can we do something with the factors of Pythagorean triple sums?

# With brute force, we'd need to check every realistic split for 1,500,000 different numbers. That's a lot. 
# (With a^2 + b^2 = c^2, and n = a + b + c, we'd need to check every c below n/2, every b below c, and every a below b.)

# All triples take the form a = m^2 - n^2, b = 2mn, c = m^2 + n^2
# Meaning that a + b + c = 2*m^2 + 2mn
# Can we generate numbers this way? m > n, so that a is a positive length
# m = 2, n = 1, sum = 12, we have 3, 4, 5
# m = 3, n = 1, sum = 24, (6, 8, 10) (not primitive)
# m = 3, n = 2, sum = 30, (5, 12, 13)

# Okay, so if we look at all m and n combinations where 2*m^2 + 2mn <= 1,500,000, that should work -- just exclude any sum that comes up twice
# (Hopefully, this is fast enough...)
# Upper limit of m at n = 1, 2*m^2 + 2m <= 1,500,000, so 2m(m + 1) <= 1,500,000, m(m + 1) <= 750,000, m <= 865

from math import sqrt, floor
from sympy import gcd

limit = 1500000

sums = [0]*(limit + 1) # Is using a list this large pratical? This may be the slowest part of the code right now (that can be adjusted to some other structure)

for m in range(2, floor(sqrt(limit/2))): # See calculation above for setting range
	for n in range(m - 1, 0, -2):
		if gcd(m, n) == 1:  # We only want primitives, which requires that m and n be coprime
			triangle_sum = 2*m*m + 2*m*n
			for k in range(1, floor(limit / triangle_sum) + 1):
				# placeholder = k*triangle_sum # Removing this seems to cut time by ~5%
				sums[k * triangle_sum] += 1 

# print(sums)
print(sums.count(1)) # Only look at sums that came up exactly once
# Takes about 17 seconds, and it's correct!

# Ways to make this faster:
# Just start n at m-1 and skip by twos: If n and m are both even or both odd, we don't get a primitive
# (adjusted code for that, though it didn't get much faster)

# Generate triples using a formula that iterates off the previous triple:
# https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples (someone in the forum had a good fast implementation of this)

