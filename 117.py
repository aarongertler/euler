# Using a combination of black square tiles and oblong tiles chosen from: 
# red tiles measuring two units, green tiles measuring three units, and blue tiles measuring four units, 
# it is possible to tile a row measuring five units in length in exactly fifteen different ways.

# How many ways can a row measuring fifty units in length be tiled?

# Should be a pretty simple combination of the previous three problems.

# Ways to tile rows of length X (including blank row):

# 1: Blank row only, total = 1
# 2: 1 (2), total = 2
# 3: 2 (2), 1 (3), total = 4
# 4: 3 (2), 2 (3), 1 (4), 1 (2 + 2), total = 8
# 5: 4 (2), 3 (3), 2 (4), 3 (2 + 2), 2 (3 + 2), total = 15
# 6: New way of counting! 2 (add 4 on the left, 2 options for remaining 2 tiles) + 4 (add 3 on the left)
	# + 8 (add 2 on the left) + 15 (add 1 on the left)

# Another way to think of it: How many ways can 50 be the sum of any number of 1s, 2s, 3s, and 4s, with permutations allowed?

# ...nah, let's try working it out like we did the others. Here's our array (not including the blank row):

# [1, 2, 4, 8, 15, 29]

# Whenever we add another tile, we get four more options for fitting in a single block (one more space on the left edge to place a one, two, three, or four)
# and we get to add the options of x - 1, x - 2, x - 3, and x - 4 

def F(L): 
	ways = [1, 2, 4, 8, 15] + [0] * (L-4)
	for i in range(5, L + 1):
		ways[i] = sum(ways[i-4:i])
	print(ways[L - 1]) # Remember indexing!

F(50)
