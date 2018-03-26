# The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.

# The set is cyclic, in that the last two digits of each number is the first two digits 
# of the next number (including the last number with the first).
# Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882),
# is represented by a different number in the set.
# This is the only set of 4-digit numbers with this property.

# Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type:
# triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.


# What do six cyclic numbers look like?

# Take six two-digit numbers, a, b, c, d, e, f
# And the cyclic numbers are ab, bc, cd, de, ef, and fa

from math import sqrt, ceil, floor

# Note: You could standardize these checks a bit more...

def triangle_check(n):
	x = 2*n
	if floor(sqrt(x)) * ceil(sqrt(x)) == x:
		return True
	else:
		return False

for n in range(19, 59):
	seed = n * (3*n - 2)
	seeds.append(seed)

# print(seeds)

def square_check(n):
	return sqrt(n).is_integer()

def pentagon_check(n):
	x = 2*n
	root = ceil(sqrt(x / 3))
	if x == (3 * root**2 - root):
		return True
	else:
		return False

# print(pentagon_check(2882)) # Checks out so far

def hexagon_check(n):
	root = ceil(sqrt(n / 2))
	if n == root * (2*root - 1):
		return True
	else:
		return False

def heptagon_check(n):
	x = 2*n
	root = ceil(sqrt(x / 5))
	if x == (5 * root**2) - (3 * root): # We could also just "return" this statement, since it has a truth value
		return True
	else:
		return False

def octagon_check(n):
	root = ceil(sqrt(n / 3))
	if n == root * (3*root - 2):
		return True
	else:
		return False

# print(heptagon_check(18))
# print(octagon_check(21)

# All of our checks work: Now, let's generate cyclic numbers. Nested loops probably simplest...
# ... but if we do something like the below, we'll probably fail, because there's no guarantee that 
# the triangular number is "next to" the square number in the cycle

# for a in range(10,99):
# 	for b in range(10,99):
# 		for c in range(10,99):
# 	  	for d in range(10,99):
# 	  		for e in range(10,99):
# 	  			for f in range(10,99):
# 	  				if (triangle_check(100*a + b) and square_check(100*b + c) and
# 	  					pentagon_check(100*c + d) and hexagon_check(100*d + e) and
# 	  					heptagon_check(100*e + f) and octagon_check(100*f + a)):
# 	  					sum = 100*(a + b + c + d + e + f) + (a + b + c + d + e + f)
# 	  					print("The sum is: ", sum) break


# New attempt: We know there's an octagonal number in the set, and there aren't many of those, so we
# can reduce our possibility space by starting with an octagonal "seed"

# Smallest four-digit octagonal is 1045 (19 oct), biggest is 9976 (58 oct)

checks = [triangle_check, square_check, pentagon_check, hexagon_check, heptagon_check]
seeds = []


# Try doing recursively: Don't keep creating lists, but call a new function with a list of checks that doesn't include the successful one?

for seed in seeds:
	a = floor(seed / 100) # first two digits
	b = seed % 100 # last two digits
	for c in range(10,99):
		cand = b*100 + c
		c_checks = list(checks)
		for check in checks:
			if check(cand):
				c_checks.remove(check)
				# print("Remaining checks: ", c_checks)
			for d in range(10,99):
				cand = c*100 + d
				d_checks = list(c_checks)
				for check in c_checks:
					if check(cand):
						d_checks.remove(check)
						# print("Remaining checks: ", d_checks)
					for e in range(10,99):
						cand = d*100 + e
						e_checks = list(d_checks)
						for check in d_checks: 
							if check(cand):
								e_checks.remove(check)
								# print("Remaining checks: ", e_checks)
							for f in range(10,99):
								cand = e*100 + f
								f_checks = list(e_checks)
								for check in e_checks: 
									if check(cand):
										f_checks.remove(check)
										# print("Remaining checks: ", f_checks)
										if f_checks[0](f*100 + a):
											sum_two_digits = a + b + c + d + e + f
											print("Found an answer!")
											print(sum_two_digits * 101) # We're adding all six numbers and 100 * each of the six
											break

# This should work eventually, but it is miserably, miserably slow, compared to answers that just generate all the "special" numbers beforehand. I'll try again in a different file.


# Based on the below, creating a list of functions *should* work:

# def add(x, y):
# 	return x + y

# def add_2(y, x):
# 	return y + x

# fns = (add, add_2)

# for fn in fns:
# 	print(fn(3, 4)) # -> 7, 7





