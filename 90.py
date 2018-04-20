# Each of the six faces on a cube has a different digit (0 to 9) written on it; 
# the same is done to a second cube. 

# By placing the two cubes side-by-side in different positions we can form 
# a variety of 2-digit numbers.

# For example, the square number 64 could be formed: 6 4


# In fact, by carefully choosing the digits on both cubes it is possible to 
# display all of the square numbers below one-hundred: 
# 01, 04, 09, 16, 25, 36, 49, 64, and 81.

# For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} 
# on one cube and {1, 2, 3, 4, 8, 9} on the other cube.

# However, for this problem we shall allow the 6 or 9 to be turned upside-down
# so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows 
# for all nine square numbers to be displayed.

# In determining a distinct arrangement we are interested in the digits on 
# each cube, not the order.

# {1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
# {1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

# But because we are allowing 6 and 9 to be reversed, the two distinct sets 
# in the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9}
# for the purpose of forming 2-digit numbers.

# How many distinct arrangements of the two cubes allow for all of the square 
# numbers to be displayed?




# This problem is all about defining how the "dice" work.
# We represent the dice as two arrays of size 6 or 7 (if the die has a 6 on it,
# since it will also have a 9 in that case).

# Because 9 is "free", any die with a 6 can also have 5 non-9 numbers.
# (Though we may not actually want to lock that in, since it reduces the number
# of distinct arrangements we can find).


# We get to start with the following dice:

# [0, , , , , ] and [1, 4, 6/9, , , ]

# (We need 1, 4, and 9 to be on a separate die from our zero die)

# Other rules:
# * If one die has a 2, the other needs to have a 5
# * If one die has a 3, the other needs to have a 6
# * If one die has a 4, the other needs to have a 9 (if we can make 49, we can always make 64)
# * If one die has a 1, the other needs to have an 8

# These don't apply if two dice share a number (if both have 2, either can have 5).


# Based on the dice above, we have eight open slots
# We can add 2, 3, 5, and 8 to four of those slots (8! / 4!)
# For the other four slots: The die with 0 must have a 4, a 6, or a 9
# The die without 5 must have a 2, or without 2 must have a 5
# The die without 1 must have an 8, or without 8 must have a 1

# ... but hard-coding all these rules leads to something very messy.
# What if we used brute force instead, and forgot about "dice rules"?


# Looking up "combinations Python" takes me to itertools.

from itertools import combinations

# test = list(combinations([1,2,3,4], 2)) # (1, 2), (1, 3), (1, 4)...
# print(test)

dice = list(combinations([0,1,2,3,4,5,6,7,8,6], 6)) # 9 and 6 are exactly the same for our purposes

# print(dice[0:4])

# Now that we have our collection of dice (only 210 of them!), we can easily check which ones match up


# Note on "targets": You caused yourself a lot of trouble by writing (0,9) instead of (0,6)...
targets = [(0,1), (0,4), (0,6), (1,6), (2,5), (3,6), (4,6), (8,1)] # (4,6) and (6,4) are equivalent, and (4,6) stands in for (4,9)

def working_pair(die_1, die_2): # In retrospect, I found that Dreamshire had a one-line way to write this!
	for a, b in targets:
		if (a in die_1 and b in die_2) or (b in die_1 and a in die_2): # Find whether we can place the two dice side-by-side to form each of our square combinations
			continue
		else:
			return False
	return True

count = 0

for i, die_1 in enumerate(dice): # Enumerate gives us a convenient way of checking the rest of the dice (rather than removing each die from the list when we finish with it, though that would also work)
	for die_2 in dice[i + 1:]: # For each die we look at, only check it against dice we haven't looked at yet, so we don't check the same combination twice
		if working_pair(die_1, die_2):
			count += 1

print("Working pairs:", count)

