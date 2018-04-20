# Too many pictures to copy and paste

# Summary: If we plot three points, one at the origin, in a 50-by-50 grid,
# How many different right triangles can we form?


# (Note: In their example, exactly 14 right triangles can be formed out of 56 possible triangles; a consistent ratio?)


# A 50-by-50 grid means that there are 51 * 51 points to plot at (minus one, for the origin)

# This should be rather easy to brute-force, though I might look for a clever solution later

from math import sqrt
from itertools import product

def distance_squared(coordinate_1, coordinate_2): # Returning this squared to avoid awkwardness with floats and rounding
	x_diff = coordinate_1[0] - coordinate_2[0]
	y_diff = coordinate_1[1] - coordinate_2[1]
	return x_diff**2 + y_diff**2

# print(distance_squared([0,0], [1,1])) # 2
# print(distance_squared([0,0], [3,4])) # 25

def right_triangle_check(coordinate_1, coordinate_2, coordinate_3): # Check if any three coordinates form a right triangle
	d1, d2, d3 = distance_squared(coordinate_1, coordinate_2), distance_squared(coordinate_1, coordinate_3), distance_squared(coordinate_2, coordinate_3)
	lines = sorted([d1, d2, d3])
	if lines[2] == lines[0] + lines[1]: # c^2 = a^2 + b^2
		# print(coordinate_1, coordinate_2, coordinate_3)
		return True
	else:
		return False

# print(right_triangle_check([0,0],[0,2],[2,2])) # True

coordinates = list(product(range(0,51), repeat = 2))
coordinates.remove((0,0)) # We can't pick the origin as a point


solutions = sum(1 for i, point_1 in enumerate(coordinates)
									for point_2 in coordinates[i + 1:] # Make sure we never double up on the same coordinate
										if right_triangle_check(point_1, point_2, (0,0)))

print("Answer:", solutions) # Checked, and this works for a 2x2 grid -- and the answer! (~9 seconds, quite slow, but within reason)



# Ways to make this faster:
# 1. Define a separate "distance from origin" function
# 2. Find some mathematical law that describes how many triangles you can find
	# (easy to count those with points on both edges, and those with points (0,x) or (x,0) and (x,x), other cases are trickier)
# 3. Use various good ideas from the Euler forum (my favorite: for every line, you can form a right angle with a perpendicular line 
	# and check all the points in the grid that lie on that line, letting you skip almost all of the brute-force checks)