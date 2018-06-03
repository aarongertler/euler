# A row measuring seven units in length has red blocks with a minimum 
# length of three units placed on it, such that any two red blocks 
# (which are allowed to be different lengths) are separated by at least 
# one black square. There are exactly seventeen ways of doing this.

# How many ways can a row measuring fifty units in length be filled?

# Add one more way ("blank row") to all the below

# Row of 1, 2: 0 ways
# Row of 3: 1 way (length 3)
# Row of 4: 2 ways (length 3) + 1 way (length 4)
# Row of 5: 3 ways (3) + 2 ways (4) + 1 way (5)
# Row of 6: 4 (3) + 3 (4) + 2 (5) + 1 (6)
# Row of 7: 1 (two 3s) + 5 + 4 + 3 + 2 + 1
# Row of 8: 3 (two 3s) + 2 (3 and 4) + 6 + 5 + 4 + 3 + 2 + 1

# Imagine starting with a row of 50. We place a block length x at the edge of that row.
# Now we have to find the number of ways to fill a space 50 - x, for any length x we use

# Sample "ways" array: [1, 1, 2, 4, 7, 11, 17] <- "17" represents "look at the previous pattern, but add 1 extra for the 3-3 split"

def n_ways(length):
	ways = (length + 1) * [0] # Ignoring the "empty row" possibility until the end, for simplicity
	for i in range(3, length + 1):
		ways[i] = ways[i - 1] + i - 2
		if i > 6:
			ways[i] += sum(ways[2:i-3])
	print(ways[length] + 1)

n_ways(50) # Piece of cake!