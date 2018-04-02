# Instructions: See #81, but now you can move up, down, and right
# You can also start anywhere in the left column, and finish anywhere in the right column
# So we'll want to find minimum path sums for all cells in that column

# But I think the same general principle should apply. Let's see!

# The order in which to set "accumuluated sums":
# The left column stays the same, since you can just start with any of those numbers
# Let's try thinking one column at a time
# For the next column to the right, each sum is (number in the second column)
# + (minimum of ...), where (...) is all the ways we could get there
# For a 3x3 matrix, for example, (2,1) can be reached the following ways:
# (1,1) + (2,1)
# (1,2) + (2,2) + (2,1)
# (1,3) + (2,3) + (2,2) + (1,1) # We wouldn't go from 1,3 to 1,2, since that just adds a number to the previous path for no reason

# We can't just assign values as we go, though, since we need to calculate all numbers in our column the same way
# We can't replace (2,1) with a path sum before we've calculated (2,2), since (2,1) might factor in

# For that reason, we'll want to build a second matrix as we go, to have an easy way of storing values from our previous matrix

# This may take too much time -- we're calculating 80*80 sums per column, with a lot of steps for each sum -- but it's a starting point

test_matrix = [[131,673,234,103,18],
							 [201,96,342,965,150],
							 [630,803,746,422,111],
							 [537,699,497,121,956],
							 [805,732,524,37,331]]

# Smoother way to load the matrix:

file = open('p082_matrix.txt', 'r')
big_matrix = [[int(x) for x in file.readline().split(',')] for i in range(80)]
file.close()

# with open("p082_matrix.txt") as f:
# 	big_matrix = f.read()
# f.closed

# big_matrix = list(big_matrix.split('\n'))
# del(big_matrix[-1]) # Get rid of trailing space

# for i in range(0, len(big_matrix)):
# 	row = big_matrix[i]
# 	row = row.split(',')
# 	row = [int(k) for k in row]
# 	big_matrix[i] = row 




def min_path_3(matrix):
	rows = len(matrix)
	columns = len(matrix[0])
	blank_matrix = []
	for b in range(0, rows):
		blank_matrix.append([0]*columns) # Create blank matrix to load path sums
	for i in range(1, columns):
		for j in range(0, rows):
			path_options = [0]*rows
			path_options[j] = matrix[j][i - 1] # Represents the fact that we can just start one step to the left of our space
			for k in range(0, j): # path_options[k] represents the sum of the path if we start one step to the left in row k, then move "down" to j
				row_counter = k
				path_options[k] += matrix[k][i - 1] # Add the value of our starting point for this path
				while j - row_counter > 0:
					path_options[k] += matrix[row_counter][i] # travel "down" to our chosen spot, adding numbers along the way
					row_counter += 1
			for l in range(j + 1, rows): # path_options[l] represents the sum of the path if we start one step to the left in row l, then move "up" to j
				row_counter = l
				path_options[l] += matrix[l][i - 1]
				while row_counter - j > 0:
					path_options[l] += matrix[row_counter][i] # travel "up" to our chosen spot, adding numbers as we go
					row_counter -= 1
			blank_matrix[j][i] = matrix[j][i] + min(path_options) # Whatever our smallest path was, add it to our current number to find the lowest accumulated sum
		for m in range(0, rows):
			matrix[m][i] = blank_matrix[m][i] # Once we've safely filled in a row on our blank matrix, and gotten all the possible sums, move it back into our original matrix

	result = 10**10
	for r in range(0, rows):
		result = min(result, matrix[r][columns - 1])

	return result

print(min_path_3(big_matrix)) # Works like a charm! Takes a couple of seconds, though, which doesn't bode well for #83...

# Ways to do this faster:

# Lots of quicker solutions in the forum. Different paths to explore:
# 1. Use memoization to avoid the need for a blank matrix (this takes 1/50th as long as your code)
# 2. Get rid of the "row counter" stuff and use statements like sum(matrix[j][i] for j in range...)
	# That's just a cleaner way to move around the matrix
