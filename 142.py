# Find the smallest x + y + z with integers x > y > z > 0 such that x + y, x − y, x + z, x − z, y + z, y − z are all perfect squares.


# What tricks do we know about finding numbers that are equidistant from two perfect squares?

# x must be in the middle of two different perfect square pairs, which themselves must have some special property...
# Maybe we try and find candidates for x first, to see if we can spot any patterns?


# Start with a list of squares, find the midpoint in each case, see if any "midpoints" are shared?

from math import sqrt

limit = 1000

# squares = list(map(lambda x: x**2, range(1, limit)))

# x_opt = []
# y_opt = []
# z_opt = []

# print(squares)

def square_test(d1, d2):
	if d1 > d2:
		y, z = d1, d2
	else:
		y, z = d2, d1
	if sqrt(y + z) % 1 == 0:
		if sqrt(y - z) % 1 == 0:
			return True

# for i, square in enumerate(squares):
# 	for square_2 in squares[i+2::2]: # Step by two, any working midpoint must be an integer
# 		midpoint = (square + square_2) / 2
# 		diff = midpoint - square
# 		if midpoint in x_opt:
# 			ind = x_opt.index(midpoint)
# 			diff_1 = y_opt[ind]
# 			diff_2 = diff
# 			# print("Testing", diff_1, "and", diff_2, "for x = ", midpoint) # Checking a (y, z) pair to see if it works
# 			if square_test(diff_1, diff_2):
# 				print("Answer:", [x_opt[ind], diff_1, diff_2].sort())
# 				break
# 		else:
# 			x_opt.append(midpoint)
# 			y_opt.append(diff)

# Works pretty quickly for low ranges, but we're not getting an answer in those ranges


# Another possible approach: We know that the difference between squares a^2 and b^2
# will be (a - b)*(a + b) (e.g. diff between 5^2 and 10^2 = 5 * 15)

# So any integer that is (a - b)*(a + b) / 2 will be a working option for x (this requires that a and b both be even or odd)
# Let me try and rewrite the first function to speed it up a bit:

# for a in range(1, limit):
# 	for b in range(a + 2, limit, 2):
# 		diff = (b + a)*(b - a) / 2
# 		x = a**2 + diff
# 		if x in x_opt:
# 			ind = x_opt.index(x)
# 			y = y_opt[ind]
# 			# print("Testing", y, "and", diff, "for x = ", x)
# 			square_test(diff, y)
# 		else:
# 			x_opt.append(x)
# 			y_opt.append(diff)

# A bit faster, nothing revolutionary, still not hitting the answer

# This calls for more math!

# We need to find numbers such that two different pairs (a, b) will have the same midpoint under our conditions
# Maybe it's better just to find every x candidate first, then test them by adding/subtracting to see if we hit two pairs of squares?

# How many candidates will we get for such a measure? (After some measurement, over 60,000 midpoints we see at least twice when testing 1 to 1000, that's too many)

# x_opt = set()
# serious_x = set()


# Notably, we're trying to find cases where a diff is also an x


# This approach stores possible y/z values indexed to their x value (but we get a gigantic array from that result)

# options = [[]]*(limit**2)
# print(len(options))

# for a in range(1, limit):
# 	for b in range(a + 2, limit, 2):
# 		diff = (b + a)*(b - a) / 2
# 		x = int(a**2 + diff)
# 		options[x].append(diff)

# for option in options:
# 	if len(option) > 2:
# 		print(option) # Well, that's a very large array stacked with candidates to sort through...


# Let's try thinking about what we know of these six values that must be square.
# They are: x-y (a), x+y (b), x-z (c), x+z (d), y-z (e), y+z (f)
# b - c = y + z = f
# d - a = y + z = f
# b - f = x - z = c
# d - f = a
# d + e = b
# a + f = d

# x = a + b / 2
# y = e + f / 2
# z = d - c / 2


# (The beginning of MathBlog.dk's post on this inspired me, and helped me think more clearly about reasonable limits)


# So we get these sets of... Pythagorean triples, maybe? Still feels off.
# If we know d and b, we can find e. If we know a and d, we can find f. If we know b and f, we can find c.

# So what we really need to know is a, b, and d. Those can give us our other numbers (and once we have all six, knowing x/y/z is trivial).

def square(n):
	return sqrt(n) % 1 == 0 # Hopefully our numbers don't get so big that this stops working...


e_checks = 0
# The below moves in ranges such that we find the smallest working value of x + y, which should correspond to the smallest working value of z
for i in range(4, limit): # x + y can't be smaller than 4, or z would be too small
	b = i**2
	for j in range(3, i):
		d = j**2
		e = b - d
		if square(e):
			e_checks += 1
			start = 2 if e % 2 == 0 else 1 # Need e and f to both be even or both be odd, so that y is an integer
			for k in range(start, j, 2): # Now we're finding y + z, the smallest square of the "adding stuff together" squares
				f = k**2
				c = b - f
				a = d - f
				if square(c):
					if square(a):
						x = (a + b) / 2
						y = (e + f) / 2
						z = (d - c) / 2
						break

# print("Vars:", a, b, c, d, e, f)
print("Times we checked e:", e_checks)
print("Answer:", x, y, z, x + y + z)

# Interesting that this approach is so much faster! I guess that not having to store and loop over a giant array is helpful.
# Also, we get to stop a LOT of investigations early by checking only square values of "e", that's much faster than the index stuff we were looking at before.
# For comparison, we only look at 1756 values of e, rather than investigating tens of thousands of duplicate x values





