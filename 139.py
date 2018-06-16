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

limit = 10**3
total = 0

def square(n):
	return sqrt(n) % 1 == 0

def tile(bigger, smaller):
	return square(bigger / smaller)

# Pythagorean generator from 75.py:

for m in range(2, floor(sqrt(limit / 2))): # Double-check this limit if you aren't getting a working answer
	for n in range (m-1, 0, -2):
		long_side = m**2 + n**2
		short_side = 2*m*n
		med_side = m**2 - n**2
		tri_area = m * n * (m**2 - n**2) # b = 2mn, a = m^2 - n^2, area = a*b / 2
		big_area = long_side**2
		small_area = big_area - (4 * tri_area)
		print("Testing a square of", big_area, "with an inner square of", small_area)
	if tile(big_area, small_area):
		print("Triangle sides:", short_side, med_side, long_side, "Square area:", small_area)
		total += 1

print("Total:", total)


# Getting weird results here. Can we add any more math to the tiling condition?

# The area of the big square = a**2 + b**2 (since c = the root of that, but then we square c)
# The area of the small square = (a - b)**2 (where a is the longer of the two short sides)
# So we need to find that a**2 + b**2 can be tiled by a**2 - b**2 - 2ab
# Editing the above equation to reflect this
