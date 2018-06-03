# A row measuring n units in length has red blocks with a minimum length of m units placed on it, such that any two red blocks 
# (which are allowed to be different lengths) are separated by at least one black square.

# Let the fill-count function, F(m, n), represent the number of ways that a row can be filled.

# For example, F(3, 29) = 673135 and F(3, 30) = 1089155.

# That is, for m = 3, it can be seen that n = 30 is the smallest value for which the fill-count function first exceeds one million.

# In the same way, for m = 10, it can be verified that F(10, 56) = 880711 and F(10, 57) = 1148904, so n = 57 is the least value 
# for which the fill-count function first exceeds one million.

# For m = 50, find the least value of n for which the fill-count function first exceeds one million.



# Shouldn't be too hard. Just need to adjust the parameters so that we start filling whenever we hit the appropriate length

def F(m,n):
	ways = (n + 1) * [0] # Ignoring the "empty row" possibility until the end, for simplicity
	for i in range(m, n + 1):
		ways[i] = ways[i - 1] + i - m + 1
		if i > 6:
			ways[i] += sum(ways[m-1:i-m])
	return ways[n]

# F(10, 56) # Works

q = 60
while F(50, q) < 10**6:
	q += 1

print("Answer:", q) # Yep, instant answer