# Given the positive integers, x, y, and z, are consecutive terms of an arithmetic progression, 
# the least value of the positive integer, n, for which the equation, x^2 − y^2 − z^2 = n, has exactly two solutions is n = 27:

# 34^2 − 27^2 − 20^2 = 12^2 − 9^2 − 6^2 = 27

# It turns out that n = 1155 is the least value which has exactly ten solutions.

# How many values of n less than one million have exactly ten distinct solutions?


# The hard part with this problem is finding when to stop, because some extremely large values of x are possible to get n = 999999 or
# something like that. There must be some hack to fix this.

# (x - y)(x + y) = x**2 - y**2, which helps, though I don't know what odd quadratic might lead us to z**2.
# (Looks like doing anything that ends up with three squares can be... ugly:
# https://www.reddit.com/r/math/comments/5jijs9/why_is_the_sum_of_three_squares_so_vastly/)

# (x - y + z)(x + y - z) = x^2 + xy - xz - xy - y^2 + yz + zx + zy - z^2 = x^2 - y^2 - z^2 + 2zy

# This might at least give us an easier way to check reasonable value ranges

# Highest possible y: 

# Highest possible z given y:


from math import sqrt, floor

def same_diff(x, y, z):
	return x**2 - y**2 - z**2

diffs = [0] * 10**6
limit = 10**6
target = 1

for x in range(1, 10**3): # Even checking with x^3 starts to get big...
	for y in range(x - 1, (x**2 / 2), -1): # y must stay high enough that z can get us down into the right range
		for z in range(floor(sqrt(x**2 - y**2)), 0, -(x - y)):
			diff = same_diff(x, y, z)
			if diff < limit:
				diffs[diff] += 1

for diff, ind in enumerate(diffs):
	if diff == target:
		print(ind)


# Something like the above structure might be fine, if we narrow the possible values... a lot.