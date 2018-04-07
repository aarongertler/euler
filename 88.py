# A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers, 
# {a1, a2, ... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

# For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

# For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. 
# The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows:

# k=2: 4 = 2 × 2 = 2 + 2
# k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
# k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
# k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
# k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

# Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; 
# note that 8 is only counted once in the sum.

# In fact, as the complete set of minimal product-sum numbers for 
# 2≤k≤12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

# What is the sum of all the minimal product-sum numbers for 2≤k≤12000?

# k=7: 12 = 1 x 1 x 1 x 1 x 1 x 3 x 4  = 1 + 1 + 1 + 1 + 1 + 3 + 4
# k=8: 12 = 1 x 1 x 1 x 1 x 1 x 2 x 2 x 3 = 1 + 1 + 1 + 1 + 1 + 2 + 2 + 3

# Ideas for finding a pattern:
# The most ones you can have for k=N is N - 2
# If you have that many ones, you need to find a number such that (N-2) + a + b = a*b
	# You can start by checking a and b = 2, then setting each equal to 3, and so on...
	# You know when to stop and try with one fewer one if a*b > N - 2 + a + b, since making a and b larger from there will only increase the disparity
	# And you only need to check (2, 6), not (6, 2), since addition and multiplication are commutative
# If you have N - 3 ones instead, you need to find a number such that N - 3 + a + b + c = a*b*c
	# (And try repeating the pattern from there)

# This is VERY brute-force, but if it works, we can try to slim things down from there

def prod(iterable):
	product = 1
	for x in iterable:
		product *= x
	return product

def all_equals(iterable):
  return len(set(iterable)) <= 1

# test = [2]*10000
# print(prod(test))

product_sums = set() # Only count each different number once


# Below code was sort of working for some numbers, but became far too messy to work with, and I'm
# still not sure that it was mathematically sound

# def generate_ps(n): # Generate the minimal product-sum number for n
# 	solutions = []
# 	arr = [2, 2]
# 	arr.extend([1]*(n-2)) # We'll go front-to-back, not back-to-front, to make writing the code easier
# 	reset = 2 # The value we'll "reset" our numbers to once we try adding another non-1 to multiply with
# 	index = 0
# 	while True:
# 		print("Array:", arr)
# 		if (prod(arr) == sum(arr)): 
# 			print("Found a solution!")
# 			result = sum(arr)
# 			solutions.append(result)
# 			for i in range(0, index+1):
# 				arr[i] = reset  # Set everything back to 2 in advance of changing another 1 into a 2
# 			index += 1 # Our next number to change is the first 1 we haven't changed ye
# 		elif prod(arr) < sum(arr):
# 			arr[index] += 1
# 		else: # Our product outgrows our sum
# 			print("Index:", index)
# 			if all_equals(arr[:index]): # We've grown to the highest possible "matched" value of our last few numbers; now time to change a 1 into a 2 and try different combinations
# 				print("Index we checked:", arr[:index])
# 				for i in range(0, index+1):
# 					arr[i] = reset  # Set everything back to 2 in advance of changing another 1 into a 2
# 				if 1 in arr:
# 					index = arr.index(1) # Our next number to change is the first 1 we haven't changed yet
# 				else:
# 					break
# 			if index == n - 1:
# 				break
# 			arr[index + 1] += 1
# 			arr[index] = arr[index + 1] # We tried 2, x for all possible x: now we try 3, x, starting with 3, 3 (since 3, 2 is the same as 2, 3)
# 			# if arr[index] == 1: # Moving to a new "place" in the array

# 	return min(solutions)

# print(generate_ps(7))



# Stopped the above attempt, realized it would always look for a 2*x solution with the last two numbers,
# even if there were some potential better solution involving lower indices of the array not being 1

# Let's see what I can find online:

# https://www-users.mat.umk.pl/~anow/ps-dvi/si-krl-a.pdf = math paper that covers some basic rules
# Namely, the minimal product-sum is always between k and 2k, since it's larger than k ones added together
# but smaller than 1, 1... 2, k (which always works, as you can see for k = 4)

# So we can use brute force if we want to, and check all possible factorizations for numbers
# between 2 and 24000, seeing which ones create a product-sum and adding them to our set

# (This means testing everything from 2*2 to 2*12000, 3*3 to 3*8000, and so on)
# (Followed by 2*2*2, 2*2*3, and so on)
# Whenever our factorization returns a value, we can find the minimal product-sum for which it works
# For example, 2*2*2 = 8, with a length of 3 and sum of 6, so we take product - sum = 2, add two ones, and now we have product = sum,
# so we've generated a solution for 5. If this is the minimum sum for a solution, solutions[5] = 8.
# (Our "solutions" array should start with a value of 2k for all numbers, since that's a known answer)

# Eventually, we've looped through all possible solutions, so we can turn our solutions array into a set of minimum values,
# add up the set, and we're done.

# (Sadly, this is a solution I figured out after reading through some code written by others, so I don't get to solve this one.
# Good work, Euler! You've taken me out for the first time.)


