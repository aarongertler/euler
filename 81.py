# In the 5 by 5 matrix below, the minimal path sum from the top left 
# to the bottom right, by only moving to the right and down, 
# is indicated in bold red and is equal to 2427.

# (Matrix here)

# Find the minimal path sum, in matrix.txt, a 31K text file containing an
# 80 by 80 matrix, from the top left to the bottom right by only moving 
# right and down.


# This should be quite simple with dynamic programming.

# Kind of silly that the matrix example they used has the misleading property where choosing the lowest number with each step leads to the correct answer.


with open("p081_matrix.txt") as f:
	big_matrix = f.read()
f.closed

big_matrix = list(big_matrix.split('\n'))
del(big_matrix[-1]) # Get rid of trailing space

for i in range(0, len(big_matrix)):
	row = big_matrix[i]
	row = row.split(',')
	row = [int(k) for k in row]
	big_matrix[i] = row # Look up a way to do this without this step later

test_matrix = [[131,673,234,103,18],
							 [201,96,342,965,150],
							 [630,803,746,422,111],
							 [537,699,497,121,956],
							 [805,732,524,37,331]]

# print(big_matrix[0])
# print(len(big_matrix[0]))

# To find the minimum sum, start with the top-right corner
# Then, for each spot on the matrix, calculate the smallest sum we can "accumulate" by getting there
# For example, if a matrix starts out as:

# 3 4
# 7 5

# We'd rewrite it as:

# 3        7 (3+4)
# 10 (3+7) 12 (3+4+5)

# And the minimum path sum would be 12.
# To lay out our full set of "accumulated" sums, we'll start by calculating the totals for the first row and first column
# (each space there only has one possible "accumulated" sum, there's only one way to reach it)
# Then, we'll use that start to lay out everything else (one row at a time)

def min_path(matrix): # Works for any rectangular matrix
	rows = len(matrix)
	columns = len(matrix[0])
	for i in range(1, columns):
		matrix[0][i] += matrix[0][i-1]
	for i in range(1, rows):
		matrix[i][0] += matrix[i-1][0]
	for i in range(1, columns):
		for j in range(1, rows):
			matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])

	return matrix[rows-1][columns-1]

	# return matrix[0]

print(min_path(big_matrix))
