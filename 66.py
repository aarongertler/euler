# Consider quadratic Diophantine equations of the form:

# x^2 – Dy^2 = 1

# For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.

# It can be assumed that there are no solutions in positive integers when D is square.

# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

# 3^2 – 2×2^2 = 1
# 2^2 – 3×1^2 = 1
# 9^2 – 5×4^2 = 1
# 5^2 – 6×2^2 = 1
# 8^2 – 7×3^2 = 1

# Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

# Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.


# * * * * * * * * *

# We want to check all values of D <= 1000, but how can we narrow down x and y?

# For each value of D, check a set of y-values, and see which ones add to an actual square number
# 1000 * y^2 is a bit more than (31y)^2...
# ...never mind, we just stop when we hit a working x

# from math import sqrt

# max_x = 0

# for d in range(100, 200):
# 	print("Checking d:", d)
# 	if int(sqrt(d)) == sqrt(d): continue # Don't check perfect square values of D
# 	y = 1
# 	x = 0.5
# 	while int(x) != x: # As long as our y^2*d term isn't one less than a square number, keep going
# 		x = sqrt(1 + d*(y**2))
# 		y += 1
# 	max_x = max(x, max_x)

# print("Largest value of X:", max_x)

# This works out fine, but would probably take over an hour to get from 1 to 1000, as edge cases like 61 are extremely tedious to calculate

# Fortunately, someone else built a shortcut:

# https://en.wikipedia.org/wiki/Chakravala_method

# (Actually, this is similar to 64, in that we could use continued fractions, but let's try something else)
# (Banged my head against Chakraval for a while, went back to continued fractions)

from math import sqrt, floor

max_x = 0
result = 0

# See https://www.mathblog.dk/project-euler-66-diophantine-equation/ for more on this form of the solution
# Also, https://en.wikipedia.org/wiki/Pell%27s_equation#Example for a walk-through of the method on a small D

for dio in range(2, 1000):
	# print("Checking d:", d)
	root = int(sqrt(dio))
	if root == sqrt(dio): continue # Don't check perfect square values of D
	
	m, d, a = 0, 1, root

	hold_x = 1
	x = a

	hold_y = 0
	y = 1

	while x**2 - dio * (y**2) != 1:
		m = (d * a) - m
		d = (dio - (m * m)) / d
		a = floor((root + m) / d) # We want this number: x/y gives us our x and y solution values, where x/y is this value

		hold_x_2 = hold_x
		hold_x = x

		hold_y_2 = hold_y
		hold_y = y

		x = a*hold_x + hold_x_2 # You're constantly setting new x and y values to test, using continued fraction values to keep checking the new convergents (a)
		y = a*hold_y + hold_y_2 # You need your last two values of x and y to find the new x/y to test

	if x > max_x: 
		max_x, result = x, dio

print("Maximum value of D:", result, "Maximum minimal X:", max_x)
