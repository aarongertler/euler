# A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly,
# F, sits in the opposite corner. By travelling on the surfaces of the room the shortest
# "straight line" distance from S to F is 10 and the path is shown on the diagram.

# (Insert picture here)

# However, there are up to three "shortest" path candidates for any given cuboid,
# and the shortest route doesn't always have integer length.

# It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, 
# with integer dimensions, up to a maximum size of M by M by M, for which 
# the shortest route has integer length when M = 100. 

# This is the least value of M for which the number of solutions first exceeds two thousand; 
# the number of solutions when M = 99 is 1975.

# Find the least value of M such that the number of solutions first exceeds one million.


# How to find the shortest straight-line distance between the corners of an A x B x C cuboid:

# Let's use 6x5x3 (Euler's example) as our example.
# We have to walk in two diagonal lines.
# By the Pythagorean theorem, we see that the length of the first line is:
# a^2 = 5^2 + x^2, a = sqrt(5^2 + x^2)
# And the length of the second line is:
# b^2 = 3^2 + (6-x)^2, b = sqrt(3^2 + (6-x)^2)

# (Found the minimum with the Desmos graphing calculator to save time)
# The minimum value of a+b is found when x/(6-x) = 5/3, x = 3.75, a+b = 10

# From this, it appears that, for cuboid A x B x C, the shortest path should always be:
# sqrt(b^2 + x^2) + sqrt(c^2 + (a-x)^2), where x / (a-x) = b/c
# This means that c*x = a*b - b*x, (b+c)*x = a*b, x = a*b/(b+c)

from math import sqrt

# def shortest_path(a, b, c): 
# 	x = a*b / (b+c)
# 	return sqrt(b**2 + x**2) + sqrt(c**2 + (a-x)**2)

# # print(shortest_path(6, 5, 3)) # shortest path is the same for 6,5,3 and 6,3,5

# limit = 100
# integer_solutions = 0

# for a in range(1, limit): # To avoid rotation, A is the longest side, B the second-longest, C the shortest
# 	for b in range(a, limit):
# 		for c in range(b, limit):
# 			sp = shortest_path(a, b, c)
# 			if int(sp) == sp:
# 				integer_solutions += 1

# print(integer_solutions) # Returns a too-small answer -- are we missing certain types of path?


# Turns out that this is a well-known sequence: http://oeis.org/A143714

# Another way to think about the cuboids that work:
# If you "unfold the box", you see that you are traveling from your starting corner
# to one of two other corners, in a straight diagonal line. For an example, see:

# http://puzzles.nigelcoldwell.co.uk/three.htm

# Your diagonal line is the hypotenuse of a right triangle, the sides of which are either
# A, (B+C) or B, (A+C). If we think of A as the longer side, the A, (B+C) hypotenuse will always be shorter.
# The distance we travel is sqrt(A^2 + (B+C)^2), so if A and B+C are two legs of a Pythagorean triple, we get an integer value

# Using this idea, we get an even simpler function:

from sympy import isprime

def shortest_path_is_int(a, b, c):
	x = sqrt(a**2 + (b+c)**2)
	if int(x) == x:
		return True
	else:
		return False

# print(shortest_path_is_int(6,5,3))

limit = 2000
integer_solutions = 0

for a in range(1, limit): # To avoid rotation, A is the longest side, B the second-longest, C the shortest
	if integer_solutions > 1000000:
			print("Past one million, a =", a - 1)
			break
	if a % 100 == 0: print("Now on a =", a)
	if (isprime(a) and a >3): continue
	for b in range(1, a + 1): # This could be sped up by checking one number, bc, which is equivalent to b+c, instead of checking separate b and c values
		for c in range(1, b + 1):
			if shortest_path_is_int(a, b, c):
				# print("Working triple:", a, b, c)
				integer_solutions += 1
					

print(integer_solutions) # Had to tinker a bit -- forgot that b and c could be equal, for instance

# And now we return the right answer, so I'll go back and add a check for when we pass 1,000,000
# The response comes out clean, but takes a long time. We can speed it up by either:
# 1. Just using the rules for the sum given to us by OEIS, or:
# 2. Making our own algorithm faster by cutting off certain values of a, b, and/or c
	# For example, a can't ever be a prime number greater than 3 (adding that check now)

# Dreamshire had the clever idea of using a single "bc" value instead of b + c, since we aren't evaluating c + b separately
# They also check for (b+c) * a being divisible by 12, since a and (b+c) are two legs of a Pythagorean triple,
# and for any Pythagorean triple, we need at least one side divisible by 3 and one divisible by 4
# (they can be the same side, as with 5, 12, 13)

# For the proof of that, see: https://en.wikipedia.org/wiki/Pythagorean_triple