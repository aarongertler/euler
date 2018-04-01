# Too picture-oriented to post in Sublime Text

# Basic idea: We have the numbers 1-10, and we're adding each number once,
# to a "magic pentagon" shape, which boils down to:

# a + b + c = d + c + e = f + e + g = h + g + i = j + i + b, or:
# a + b = d + e, d + c = f + g, f + e = h + i, h + g = j + b, a + c = j + i 

# Our solution set is then described as: (a, b, c, d, c, e, f, e, g, h, g, i, j, i, b)
# But with only the digits mattering, so that we're looking for the largest possible 16-digit string

# A 16-digit string implies that, since there are 15 numbers in all, 10 is used only once
# So 10 must be a, d, f, h, or j (the "outer" numbers on the shell)

# Brute force: Start with all the permutations of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# (10! possibilities)
# Then, for each permutation, if 10 is in one of the five correct positions...
# (10!/2 possibilities),
# Check whether the addition problem above works out.
# If it does, add our permutation to a set of solutions, then find the max solution later

# I misread the problem at first -- we always count starting at the lowest number on the outer ring. So let's assume that our outer ring is 10-9-8-7-6 and we get to start with 6.
from itertools import permutations

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

perms = list(permutations(digits)) # This is pretty quick!

max_n = 0
solutions = []

# print(len(list(perm)))

for perm in perms:
	a, b, c, d, e, f, g, h, i, j = perm[0], perm[1], perm[2], perm[3], perm[4], perm[5], perm[6], perm[7], perm[8], perm[9] # There must be a shorter way to write this...
	if a == 6: # Trying to check ideal option first, see above
		if 10 == (d or f or h or j):
			if (a + b + c) == (d + c + e) == (f + e + g) == (h + g + i) == (j + i + b): # I suppose I could write an "all_equal" function to make this more flexible for other shapes
				solution = (a, b, c, d, c, e, f, e, g, h, g, i, j, i, b)
				n = int(''.join(str(x) for x in solution)) # Convert our collection of digits to a string, then to a number (could this be done faster?)
				solutions.append(n)
				if n > max_n:
					max_n = n

print(solutions)
print("Largest number:", max_n)






