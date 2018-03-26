# Too long to copy-paste

# All square roots can be written as periodic continued fractions:

# sqrt(23) = 4 + 1 / (1 + (1 /(1 + 1/(...) + 1) + 3) + 1)

# Eventually, these will all repeat: sqrt(23) is 4 + this fraction with 1, 3, 1, 8, repeating forever

# The "period" = the number of digits before we repeat (23 has a period of 4)

# How many continued fractions for N <= 10000 have an odd period?

from math import sqrt, floor

# def period(n):
# 	root = floor(sqrt(n))
# 	remainder = sqrt(n) - root
# 	next_digit = ceiling(1 / remainder)
# 	next_fraction =  sqrt(n) + root - (n - root**2) / n - root**2


# Trying the "algorithm" section of this:

# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion (thanks to Dreamshire for the link)

odd_periods = 0

for n in range(2, 10000):
	root = floor(sqrt(n))
	if root**2 == n:
		continue
	else:	
		m, d, a = 0, 1, root # Dreamshire implemented a single-variable algorithm, I'll stick to the book
		period = 0
		while a != 2*root or period == 0: # I've seen this with d != 1, not sure why that works
			m = (d * a) - m
			d = (n - (m * m)) / d
			a = floor((root + m) / d)
			period += 1
		if period % 2 == 1:
			odd_periods += 1

print("Number of odd periods:", odd_periods)

# Testing for n = 23:

# 1: 0, 1, 4
# 2: 4, 7, 1
# 3: 3, 2, 3 
# 4: 3, 7, 1
# 5: 4, 1, 8 (d is 1, terminate) (also, a is 2*4, terminate)
# 6: 4, 7, 1 (pattern begins to repeat)