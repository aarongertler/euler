# The cube, 41063625 (3453), can be permuted to produce two other cubes: 
# 56623104 (3843) and 66430125 (4053). 

# In fact, 41063625 is the smallest cube which has exactly three permutations of its 
# digits which are also cube.

# Find the smallest cube for which exactly five permutations of its digits are cube.


# Starting point: Create all the eight-digit cubes? Is that a good # of digits?

# Or just create an array/dictionary of all cube roots and their cubes, then sort the cubes, find cubes that have identical sorts
# So we might have {345: 41063625, 405, 66430125} and turn it into {345: 01234566, 405: 01234566}

# from collections import Counter

def digit_sort(x):
	x = str(x)
	return sorted(x)

cubes = []
n = 1000

while n < 10000:
	cube = n**3
	cubes.append( (n, ''.join(digit_sort(cube))) )
	n += 1

permutation_counts = {}

for cube, value in cubes:
	if value in permutation_counts:
		permutation_counts[value] += 1 # We could add a check below to return the count if permutation_counts[value] = 5, would save us from having to sort
		# permutation_counts[value] += [cube] # This is another angle we could take, and then we could sort by len(permutation_counts[value]) rather than sorting by the values themselves
	else:
		permutation_counts[value] = 1
	
# print(permutation_counts) # We've manually replicated Counter this way

sorted_counts = sorted((value, key) for (key, value) in permutation_counts.items())

print(sorted_counts) # We have two permutations that each appear five times, but this one works

for cube, value in cubes:
	if value == '012334566789' or value == '012334556789':
		print(cube) # Smallest cube in this list is 5027, which, cubed, is the answer

# print(Counter(cubes.values())) # For 10000, finds me two permutations that each appear five times



# Many, many other ways to do this, all of them too quick to distinguish

# For example, there's a nice solution from Dreamshire that iterates as it goes:

# digits, min_cube, n, d = '', float('Inf'), 1000, 5
# cubes = {} # Dictionaries are apparently the best data structure for handling this

# while min_cube == float('Inf') or len(digits) <= len(str(min_cube)): # Keep going until we've checked all cubes with the same # of digits as our cube
# 	cube = n**3
# 	digits = ''.join(sorted(str(cube)))
# 	if digits in cubes: # Check whether we've seen this pattern before
# 		cubes[digits] += [cube] # Add the cube to our collection of cubes that work for this permutation (saves a step from the above, since we save the cubes directly rather than just noting how many times a permutation has appeared)
# 		if len(cubes[digits]) == d:
# 			min_cube = min(min_cube, cubes[digits][0]) # Our smallest cube is now the smallest cube that fits the permutation we've found five times
# 	else:
# 		cubes[digits] = [cube]
# 	n += 1 # n keeps track of the number we're actually taking the cube of

# print("Smallest cube:", min_cube)


# I also liked this very minimal solution:

for i in range(1,10000):
    cubes.append(''.join(sorted(list(str(i**3)))))
    
cube_counts = []
for i in cubes:
    if cubes.count(i) == 5:
        cube_counts.append(i)
        
for i in range(1,10000):
    if ''.join(sorted(list(str(i**3)))) == cube_counts[0]: # We need to check index 1 as well, and any other indices that have a 5-time recurring permutation -- so this solution wasn't quite right
        	# Specifically, we can't guarantee that the first cube permutation we found five times also includes the lowest individual cube: The lowest cube may just share a permutation with four much higher cubes, and thus, we might only have discovered the fifth instance of that permutation late in the game
        print(i)
        print(i**3)
        break

# Even shorter!

from collections import defaultdict # Lets us assign values to keys that don't exist in the dictionary yet
cube_dict = defaultdict(list)

i = 0
while True:
    cube = i ** 3
    key = ''.join(sorted(str(cube)))
    cube_dict[key].append(cube)
    if len(cube_dict[key]) == 5:
        print cube_dict[key][0]
        break
    i += 1

