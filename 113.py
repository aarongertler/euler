# Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

# Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

# We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

# As n increases, the proportion of bouncy numbers below n increases such that there are only 12951 numbers below one-million 
# that are not bouncy and only 277032 non-bouncy numbers below 10^10.

# How many numbers below a googol (10^100) are not bouncy?


# How many *possible* non-bouncy numbers are there below 10^n?

# 10^1: 9
# 10^2: 99
# 10^3: Here's where things get interesting!

# A non-bouncy number starts with a particular number. Every other number is either the same as the previous number, or greater/smaller.
# Let's use numbers below 10^4 as an example.
# If we start with 1abc, there are 9 options for the next digit (a), then 10-a options for b, then 10-b options for c.
# For example, if we go with 13bc, b can be anything from 3-9 (7 options). If we then go with 136c, c can be anything from 6-9 (4 options).

# So the number of possible non-bouncy numbers below 10^3 is as follows:
# Start with a 1: 9 + 8 + 7 ... + 1 (9 options for 11a, 8 for 12a, etc.), plus the decreasing options, 1 + 1 (110, 100)
# Start with a 2: 8 + 7 + 6 ... + 1, plus the decreasing options, 2 + 2 + 1 (2 options for 22a, 2 for 21a, and 200)
# Start with a 3: 7 + 6 + 5 ... + 1, plus 3 + 3 + 2 + 1

# Separating into "increasing" and "decreasing" (counting "all the same digit" as "increasing"):
# Start with a 1: 9 + 8 ... + 1 increasing, 1 + 1 decreasing (= 10 + 9 + 7 6 5 4 3 2 1)
# 2: 8 + 7 ... + 1 inc, 2 + 2 + 1 dec (= 10 + 9 + 7 5 4 3 2 1)
# 3: 7 + 6 ... + 1 inc, 3 + 3 + 2 + 1 dec (= 10 + 9 + 7 5 3 2 1)
# 4: 6 + 5 ... + 1 inc, 4 + 4 + 3 + 2 + 1 dec (= 10 + 9 + 7 5 3 1)
# 5: 5 + 4 ... + 1 inc, 5 + 5 + 4 + 3 + 2 + 1 dec (= 10 9 7 5 3 1)

# How can we check more digits without a series of forking paths for each subsequent digit? We need to find a pattern.


# Aha! After sleeping on it, I realized that you can think of this problem in terms of "paths", as with Euler #15.
# If you want to find the number of decreasing 10-digit numbers that start with 5 and end with 0, you're
# finding the number of "paths" from top left to bottom right on a 9x5 grid.
# 5000000000 is like immediately going down five times, then over nine times (down to zero, then "hitting" zero nine times)
# 5544332211 is like going over one, down one, over two, down one... etc.

# Finding paths when you have two directions requires binomial expansion:
# Y! / X!(Y-X)!  --> for the above example, it would be 14! / 5!(14-5)!, because we are making 14 "moves" and 5 of those moves are "down"

from math import factorial

factorials = [1] # 0! = 1
for i in range(1, 110): # Need to account for moving over 99 times (100-digit number), and up/down at least 9 times
	factorials.append(factorial(i))

def increasing_n(first, last, digits): # First digit, last digit, # of digits
	up = last - first # Number of times you can increase your number before you hit the target
	over = digits - 1
	moves = up + over - 1 # Had to subtract 1 to make the numbers work here -- I think that because last digit is fixed, there's one less "degree of freedom"
	return factorials[moves] / (factorials[up]*factorials[moves - up])

print(increasing_n(5,7,4)) # 5557, 5567, 5577, 5667, 5677, 5777
print(increasing_n(1,8,4)) # Works, there should be sum(1 to 8) = 36 paths

def decreasing_n(first, last, digits):
	down = first - last # Number of times you can decrease your number before you hit the target
	over = digits - 1
	moves = down + over - 1 # Had to subtract 1 to make the numbers work here -- I think that because last digit is fixed, there's one less "degree of freedom"
	return factorials[moves] / (factorials[down]*factorials[moves - down])

# Let's sanity-check this using our formula from 112...

# def is_bouncy(n):
# 	status = None
# 	s = str(n)
# 	i = 1
# 	while (status != "bouncy") and i < len(s):
# 		if (s[i] > s[i - 1]) and status == None:
# 			status = "increasing"
# 		if (s[i] < s[i - 1]) and status == None:
# 			status = "decreasing"
# 		if (s[i] > s[i - 1]) and status == "decreasing":
# 			status = "bouncy"
# 		if (s[i] < s[i - 1]) and status == "increasing":
# 			status = "bouncy"
# 		i += 1
# 	return status == "bouncy"

# start = 1000
# finish = 10000
# total = 0
# for i in range(start, finish):
# 	if not is_bouncy(i):
# 		total += 1

# print("Non-bouncy numbers between", start, "and", finish, ":", total)

# total = 0
# digits = 4

# for first in range(1, 10):
# 	for last in range(1, 11): # Last digit can be zero!
# 		add = 0
# 		if last >= first:
# 			add += increasing_n(first, last, digits)
# 		if last < first:
# 			add += decreasing_n(first, last, digits)
# 		# print("Non-bouncy starting with", first, "and ending with", last, ":", add)
# 		total += add

# print("Non-bouncy numbers between", start, "and", finish, ":", total)

# Awesome! Works for four-digit numbers. Now let's try a digit range...

total = 0

for digits in range(1, 101):
	for first in range(1, 10):
		for last in range(1, 11): # Last digit can be zero!
			add = 0
			if last >= first:
				total += increasing_n(first, last, digits)
			if last < first:
				total += decreasing_n(first, last, digits)

print("Total bouncy numbers below 10^100:", total) # Works! Is it fast enough for a googol?

# Works instantly!

# Of course, Dreamshire's solution is two lines... they found a considerably faster binomial solution, with no explanation.
# (Turns out that "sum of all decreasing numbers at x digits" is just binomial(x + 10, x))

# Still, happy to have noticed the binomial path connection despite the last binomial problem happening a long time ago

