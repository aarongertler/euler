# If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, 
# and two discs were taken at random, it can be seen that the probability of taking two blue discs, 
# P(BB) = (15/21)×(14/20) = 1/2.

# The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random,
# is a box containing eighty-five blue discs and thirty-five red discs.

# By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total, 
# determine the number of blue discs that the box would contain.


# We're looking for pairs of numbers a, b such that a/(a+b) * (a-1)/(a+b-1) = 1/2
# That is, (a^2 - a)/(a^2 +ab -a + ab + b^2 -b) = 1/2
# 2a^2 - 2a = a^2 + b^2 + 2ab - a - b
# a^2 - a = b^2 + 2ab - b
# a^2 - a = b(b + 2a - 1)

# There are certain values of a for which b is a whole number.
# It would be nice if I knew enough number theory to know how to look
# up ways to track those numbers down. Instead, let's look for patterns.

# 15/21 and 85/120 are extremely similar numbers, with values close to .71
# Put another way, b/a is very close to 0.4

# Let's explore, and see whether grabbing a few more examples will help us find some kind of central value these converge to

# limit = 1000000

# for a in range(500000, limit): # Red discs
# 	for b in range(int(4141*a / 10000), int(4143*a / 10000)): # Blue discs
# 		if a**2 - a == b*(b + 2*a - 1):
# 			print("a =", a, "b =", b)

# After running some ranges with smaller numbers, 
# I notice that we tend to zero in on a particular value of a/b.
# And the pattern "0.4142..." reminds me of sqrt(2) -- we're actually converging there!

from math import sqrt

limit = 10**7
constant = sqrt(2) - 1

# for a in range(10**5, limit): # Red discs
# 	for b in range(int(a * constant) - 1, int(a * constant) + 1): # Blue discs
# 		if a**2 - a == b*(b + 2*a - 1):
# 			print("a =", a, "b =", b)

# Yep, this one hits all of our pairs when I test it on various ranges. Let's close the case.

# flag = False
# start = int(10**12 * sqrt(2)/2) # a / a+b converges to sqrt(2)/2
# a = start

# while flag == False: # This is too slow, let's try it without the range
# 	for b in range(int(a * constant) - 1, int(a * constant) + 1):
# 		if a**2 - a == b*(b + 2*a - 1):
# 			print("a =", a, "b =", b)
# 			flag = True
# 	a += 1


# The above solution was checking too many numbers. Looking for more patterns,
# I see that the ratio of each solution's a to the previous a is the same.

# 85/15 ~= 493/85 ~= 2871/493... ~= 5.8284 (can't find any special relationship of this number to the square root of 2)

# Trouble is, as the numbers get bigger, we need to keep fine-tuning our ratio, lest it lose precision
# However! We're always about 12 away from the next a if we take (present a)^2 / (previous a)
# And if we do the same thing with b, we are always right to the nearest integer (getting closer and closer every time)

b, next_b = 6, 35
flag = False
constant = (2 - sqrt(2)) / 2 # For every two disks, we have sqrt(2) blue and 2 - sqrt(2) red 

while flag == False:
	next_b, b = int(next_b**2 / b), next_b
	if (b / constant) > 10**12:
		flag = True
		print("b =", b)

# b / (2 - sqrt(2)) = a / sqrt(2)

a = round(((b * sqrt(2)) / (2 - sqrt(2))), 0)

print("a =", a) # Note: Answer is rounded up, not down, but that's not hard to check (takes < 1 second)


# Other solutions:

# You can't speed up this solution much, but another option is to use the Diophantine quadratic method, as Dreamshire did.
	# That works with a proven pattern, at least, rather than relying on the random recognition I had to use




