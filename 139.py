# Let (a, b, c) represent the three sides of a right angle triangle with integral length sides. 
# It is possible to place four such triangles together to form a square with length c.

# For example, (3, 4, 5) triangles can be placed together to form a 5 by 5 square with a 1 by 1 hole in the middle 
# and it can be seen that the 5 by 5 square can be tiled with twenty-five 1 by 1 squares.


# However, if (5, 12, 13) triangles were used then the hole would measure 7 by 7 and these could not be used to tile the 13 by 13 square.

# Given that the perimeter of the right triangle is less than one-hundred million, how many Pythagorean triangles would allow 
# such a tiling to take place?


# The math: hypotenuse^2 - 4*area = smaller square area
# And you can tile the bigger square if bigger square / smaller square is itself a square number

# As usual, let's start with brute force...


from math import sqrt, floor

limit = 10**8
total = 0

def square(n):
	return sqrt(n) % 1 == 0

def tile(bigger, smaller):
	return square(bigger / smaller)



# Insert pythagorean generator here (see 75.py)

for m in range(2, floor(sqrt(limit / 2))): # Double-check this limit if you aren't getting a working answer
	for n in range (m-1, 0, -2):
	long_side = m**2 + n**2
	tri_area = m * n * (m**2 - n**2) # b = 2mn, a = m^2 - n^2, area = a*b / 2
	big_area = long_side**2
	small_area = big_area - (4 * tri_area)
	if tile(big_area, small_area):
		total += 1

print("Total:", total)



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