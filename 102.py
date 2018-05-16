# Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

# Consider the following two triangles:

# A(-340,495), B(-153,-910), C(835,-947)

# X(-175,41), Y(-421,-714), Z(574,-645)

# It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

# Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of 
# one thousand "random" triangles, find the number of triangles for which the interior contains the origin.

# NOTE: The first two examples in the file represent the triangles in the example given above.


# Triangles which fit the description must meet the following criteria:
# The basic btute-force method is just to draw two lines and see if the origin falls between them
# At least one point must be on the opposite side of the x/y axis from the other two (that is, the points must be in three different quadrants)
# And the line between the two points surrounding the "missing" quadrant must pass through that quadrant
# For example, if we have points in quadrants I, II, and III, the line between quadrants I and III must pass through IV

# What's the fastest way to tell if a line between two points will pass through a quadrant?
# Not sure this is really "fastest", but finding a slope is easy, and once you have a slope, you just need to
# find whether you have enough horizontal/vertical distance to hit the axis at the right spot before you reach the next point.

# For example, with triangle ABC above, we need to hit quadrant I
# The slope between A and C is -1442/1175, and the relevant axis is the Y-axis
# So we have to find whether, as we drop from 495 to 0, we get enough horizontal distance to go from -340 to 0
# 495 * 1175/1442 > 340, so we do!

# But for XYZ, the slope from X to Z is -686/749, and when we drop from 41 to 0, we don't get enough horizontal distance to go from -175 to 0

# There's surely a more efficient algorithm available, but this should work as a starting point:

# triangles = open('p102_triangles.txt', 'r').read().split('\n')
triangles = open('p102_triangles.txt').read().split('\n')
print(triangles)

# for line in triangles:
# 	n = list(map(int, line.split(',')))
# 	print(n)
# 	print(n[0:2])
# 	print(n[2:4])


# print(triangles)
# print(triangles[0])
# print(triangles[0][0])


# Actually, with a bit more searching, I found a neat trick: If you want to check whether triangle ABC includes point P, you can check whether
# the areas of PAB, PAC, and PBC add up to the area of ABC
# (Source: https://www.geeksforgeeks.org/check-whether-a-given-point-lies-inside-a-triangle-or-not/)

total = 0
origin = [0,0]

def area(a, b, c):
	return abs(a[0]*(b[1]-c[1]) + b[0]*(c[1] - a[1]) + c[0]*(a[1] - b[1])) / 2

# print(area([0,0], [0,4], [6,0]))

for triangle in triangles:
	# print(triangle)
	points = list(map(int, triangle.split(',')))
	a, b, c = points[0:2], points[2:4], points[4:]
	if area(a, b, c) == (area(b, c, origin) + area(a, c, origin) + area(a, b, origin)):
		total += 1

print("Working triangles:", total) # Gives the right answer instantly, nice that this is expandable (lots of other ways to solve)