# A row of five black square tiles is to have a number of its tiles replaced with coloured oblong tiles chosen from 
# red (length two), green (length three), or blue (length four).

# If red tiles are chosen there are exactly seven ways this can be done.
 
# If green tiles are chosen there are three ways.
 
# And if blue tiles are chosen there are two ways.

# Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways of replacing the black tiles in a row measuring five units in length.

# How many different ways can the black tiles in a row measuring fifty units in length be replaced if colours cannot be mixed 
# and at least one coloured tile must be used?


# Can we find a rule that lets us start with a known length, then increase the number of solutions as the length increases?

# Blue tiles:
# Length 5 = 2 ways
# 6 = 3 ways
# 7 = 4 ways
# 8 = 5 ways (one tile) + 1 way (two tiles)
# 9 = 6 ways (one) + 3 ways (two)
# 10 = 7 ways (one) + 6 ways (two)
# 11 = 8 ways (one) + 10 ways (two) # A pattern emerges! The two tiles can be placed together (as a tile of length "8", 4 ways to add),
	# one tile apart (3 ways), two tiles apart (2 ways), or three tiles apart (one way)
	# This "triangular number" pattern will continue infinitely.
	# What happens when we add the option for a third tile?
# 12 = 9 ways (one) + 15 ways (two) + 1 way (three)
# 13 = 10 ways (one) + 21 ways (two) + 4 ways (three) # 4 = 1 + 3
# 14 = 11 + 28 + 10 ways (three) # 10 = 1 + 3 + 6 # If you keep one tile on the edge, you give the other 2 tiles a space of 10 blacks (6 options).
	# If you move it one away from the edge, you give the other 2 tiles a space of 9 blacks (3 options). If you move it two away from the edge, you give
	# the other 2 tiles a space of 8 blacks (one option).

# This pattern will continue for any number of tiles, which means we'll have to engage in some heavy-duty dynamic programming.

# We need an array that remembers certain values from the "past".
# If we want to figure out how many ways to fit two blues into ten blacks, we need to be able to check the number of ways to fit one blue
	# into six, five, and four blacks
# If we want to figure out how many ways to fit three blues into fourteen blacks, we need to be able to check the number of ways to fit
	# two blues into ten, nine, and eight blacks


ways = [[0]]

def n_ways(tile, row): # tile = length of colored tile, row = # of black tiles
	i = 0
	while i < row:
		i += 1
		ways.append([0])
		if i < tile:
			print("Ways:", ways, "i:", i)
			ways[i] = [0]
		j, count = i, 0
		while j >= tile:
			ways[i] = [j - tile + 1]
			print("Ways:", ways, "i:", i, "j:", j)
			ways[i][count] = ways[i - tile][count - 1]
			t = tile
			while t > 1:
				ways[i][count] += ways[i - t][count - 1]
				t -= 1
			count += 1
			j -= tile
	print("Ways array:", ways)
	print("Total ways:", sum(ways))

n_ways(4, 10)







