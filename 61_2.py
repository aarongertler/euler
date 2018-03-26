# The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.

# The set is cyclic, in that the last two digits of each number is the first two digits 
# of the next number (including the last number with the first).
# Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882),
# is represented by a different number in the set.
# This is the only set of 4-digit numbers with this property.

# Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type:
# triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.


# What do six cyclic numbers look like?

# Take six two-digit numbers, a, b, c, d, e, f
# And the cyclic numbers are ab, bc, cd, de, ef, and fa

# Trying to check all two-digit numbers for working cyclicality was too slow; let's start with the solutions instead.

# This was an inspiration, especially since this is my first time working in Python: https://blog.dreamshire.com/project-euler-61-solution/

def shapes(n): # Some ugly floats here, but we do get the answer
	return ("tri", n*(n+1)/2), ("square", n*n), ("pent", n*(3*n - 1)/2), \
	("hex", n*(2*n - 1)), ("hept", n*(5*n - 3)/2), ("oct", n*(3*n - 2)) # Note: Without the backslash, no 6, 7, or 8 shape numbers were being returned...

def find_chain(shapes, numbers):
	# print("Finding a chain for", shapes, "and", numbers)
	if len(shapes) == 6 and numbers[0] // 100 == numbers[-1] % 100: # Check that we have six numbers, and that the cycle is complete from the end of the last number to the start of the first
		print(numbers, sum(numbers))
	else:
		for shape, number in chains.get((shapes[-1], numbers[-1]), []): # Look at each number in our test number's chain...
			if shape not in shapes: # ...see if it's a different shape (and move to next number if no new shapes can be found)...
				find_chain(shapes + [shape], numbers + [number]) # ...and then move to the chain for the first successful number, until we recursively build a six-chain

polys = []
n = 19 # Generates the lowest 4-digit octagonal number
finish = 141 # Generates the largest 4-digit triangular number

# Generate all four-digit numbers

while n < finish:
	for shape, number in shapes(n):
		if 1000 <= number <= 9999 and number % 100 > 9: # No four-digit number can have 0x as its last two digits
			polys.append( (shape, number) )
	n += 1

print(polys)

# Build a collection of "chains" that link cyclical polygonal numbers:

chains = {}

for shape, number in polys: # For every polygonal number...
	for next_shape, next_number in polys: # ...look at all the other polygonal numbers...
		if shape != next_shape and number % 100 == next_number // 100: # ... find those that match cyclically...
			chains[shape, number] = chains.get((shape, number),[]) + [(next_shape, next_number)] # ...and create chains as you go

# By the end of the above, we'll have 1035 linked with all the 35xx numbers (for example)

for shape, number in chains: find_chain([shape], [number])