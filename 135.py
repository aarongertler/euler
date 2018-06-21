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

# Note: z = 2y - x

# Highest possible y/z: We know that y^2 + z^2 + 1,000,000 > x^2 > y^2 + z^2
# We also know that y = x - a, and z = x - 2a
# (x - a)^2 + (x - 2a)^2 = 2x^2 - 6ax + 5a^2 < x^2
# -x^2 > -6ax + 5a^2
# x^2 < 6ax - 5a^2, 0 < -x^2 + 6ax - 5a^2, 0 > x^2 - 6ax + 5a^2, 0 > (x - a)(x - 5a)
# So x - a must be positive (and x - 2a must be positive), and x - 5a must be negative.
# ...does that actually help us much? We never have to deal with x - 5a, do we?

# Highest possible x: x^2 - y^2 - z^2 ~= 999,999, when y = x-1 and z = x-2
# So x^2 - (x - 1)^2 - (x - 2)^2 ~= 999,999
# = x^2 - x^2 + 2x - 1 - x^2 + 4x - 4
# = -x^2 + 6x - 5 = (-x + 1)(x - 5)... something's off here, this doesn't allow very large x values at all
# So we actually want a big spread to get a "safe" x value
# See above -- find a case where x**2 - (x - a)(x - 5a) can't be between 1000000 and 0 for some value of x

# Hm. The above line translates to x**2 - x**2 + 6ax - 5a**2 = 6ax - 5a**2
# So now we want to look at all the values of a and x that allow this to give us an answer between 0 and 10**6
# With a between 1 and ceil(x / 2) - 1
# And with x seeming to be... almost unlimited? Needs more thought.


# limit = 10**6

# while flag == False:
# 	x += 1
# 	while 


# https://en.wikipedia.org/wiki/Congruum is almost helpful, but feels unrelated -- it finds squares that are equally far apart,
# without specifying anything about what happens when you square numbers that are equally far apart.


from math import sqrt, floor

def same_diff(x, y, z):
	return x**2 - y**2 - z**2

diffs = [0] * 10**6
limit = 10**6
target = 10

for x in range(1, 10**4): # Even checking with x^3 starts to get big...
	for y in range(x - 1, floor(sqrt(x**2 / 2)) + 1, -1): # y must stay high enough that z can get us down into the right range
		z = 2*y - x
		diff = same_diff(x, y, z)
		if diff < limit:
			diffs[diff] += 1

total = 0
for ind, diff in enumerate(diffs):
	if diff == target:
		total += 1

print("# of answers:", total)
print(diffs[0:100])


# Something like the above structure might be fine, if we narrow the possible values... a lot.