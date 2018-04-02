# A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

# For example,

# 44 → 32 → 13 → 10 → 1 → 1
# 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. 
# What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

# How many starting numbers below ten million will arrive at 89?

def sum_of_squares_of_digits(n):
	result = 0
	while n > 0:
		result += (n % 10)**2
		n = n // 10
	return result

# print(sum_of_squares_of_digits(1234))

limit = 10000000
count = 0

for i in range(2, limit):
	s = sum_of_squares_of_digits(i)
	while s != 1 and s != 89 and s != 4: # 4 leads to 89 and is a common sum, so we save a few steps here (see "Unhappy Numbers", Wikipedia)
		s = sum_of_squares_of_digits(s)
	if s == 89 or s == 4: count += 1

print(count) # Answer takes about 30 seconds

# Ways to make this (much) faster:

# 1. clearly, 123456 and 654321 will return the same result. So we really only need to check numbers with unique sets of nonzero digits.
# 2. You can also know that the maximum square sum will be 9^2 * 7 (567), since 9999999 is the number with the largest possible digit sum in our set.
	# This means we can build a table of 567 numbers and, as we hit examples of those numbers, check whwether they arrive at 89.
	# Once we have a number saved, e.g. table[233] = True, we only need to run sum_of_squares once for any number whose square sum is saved.
	# This would be very simple to code if I ever feel like revisiting the problem.


