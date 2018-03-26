# By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles.

# Although there exists no rectangular grid that contains exactly two million rectangles, 
# find the area of the grid with the nearest solution.


# Formula for the number of rectangles:

# Number of "spaces" (rows * columns) + number of rows + number of columns + 1
# Plus the smaller rectangles, which means: 

# For a small A x B rectangle, it can fit into a large M x N rectangle as follows:
# Going in "horizontally" (A and M are horizontal dimensions), (A + 1 - M) * (B + 1 - N)
# Going in "vertically", (A + 1 - N) * (B + 1 - M)
# For example, a 2x1 goes into a 3x2 four times "horizontally" (2 * 2) and three times "vertically" (3 * 1)
# And a 2x2 goes into a 3x2 twice (3 + 1 - 2) * (2 + 1 - 2) (but we don't double-count it, because it doesn't rotate)


# Note: You struggled with the formula a bit because you only tested 3*2 and 3*3, not 2*4. Broaden your horizons!

def rectangles(a, b): # Count smaller rectangles that fit into a large A x B rectangle
	count = 0 # The loop below catches everything, including 1 x 1 rectangles and the whole rectangle
	for m in range(1, a+1):
		for n in range(1, b+1): # Had a range of m to b+1 before, but 3x1 works differently than 1x3!
			count += (a + 1 - m) * (b + 1 - n) # We'll count 1x1 once, 2x1 once, 1x2 once --> that's the right move
			# print("Counted", m, "and", n, "there are now", count, "rectangles")

	return count

# print(rectangles(50,60)) # This is close to 2 million, I'll set a range of 100 as a starting point

min_difference = 1000000
min_x, min_y = 0, 0

for x in range(1, 100):
	for y in range(x, 100): # Don't double-count any sizes
		difference = abs(rectangles(x, y) - 2000000)
		if difference < min_difference:
			# print("New difference found:", difference, "for x=", x, "and y=", y) 
			min_difference = difference
			min_x = x
			min_y = y

print("Minimum difference at X =", min_x, "Y =", min_y, "area =", min_x * min_y)

# This gets the answer in less than 3 seconds, but there's math to make it faster:

# Sum(1..X) = (x^2 + x) / 2
# Summing up the rectangles in an A x B grid means we multiply the sum of the counting numbers for each dimension
# For example, a 5 x 7 would be (25 + 5)/2 * (49 + 7)/2

# The reasoning behind this is a lot of fun! For example, if we look at a 2 x 4 rectangle...
# ...we can multiply counting sums to find 1*1 + 1*2 + 1*3 + 1*4 + 2*1 + 2*2 + 2*3 + 2*4
# Each term in this equation describes the number of rectangles of the INVERSE size.
# For example, there is 1*1 = 1  2*4 rectangle, and there are 1*3 = 3 2*2 rectangles

# This matches up perfectly with the manual math we were doing: For each rectangle of a given size, we multiply by the inverse of those sizes to get the total # of rectangles
# And it just so happens that doing this math is the same as multiplying (1 + 2 ... + A)*(1 + 2 ... + B)

