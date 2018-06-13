# Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. 
# For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. 
# Leading zeroes are not allowed in either n or reverse(n).

# There are 120 reversible numbers below one-thousand.

# How many reversible numbers are there below one-billion (10^9)?


# ...this feels like it should be brute-forceable? (Maybe we can find a quick way to knock out half our numbers for a bit of bonus speed.)

import math

def get_digit(n, d): # https://stackoverflow.com/questions/39644638/how-to-take-the-nth-digit-of-a-number-in-python
	return n // 10**d % 10

def reversible(n):
	if n % 10 == 0: # no leading zeroes!
		return False
	rev = int(str(n)[::-1])
	s = n + rev
	l = len(str(s))
	for d in range(0, l):
		if get_digit(s, d) % 2 == 0:
			return False
	print(n, "is reversible, the reverse is", rev, "and the sum is", s)
	return True

# print(reversible(409))
# print(reversible(408))

lower = 10**9 - 10**7
limit = 10**9 # Brute force becomes impractical right around one million
count = 0

for i in range(lower, limit):
	if reversible(i):
		count += 1

print(count)


# Other questions to ask:

# How many total *possible* reversible sums exist below two billion? And then, how many can we reach with actual addition?
# What are the properties of the sums of n + reverse(n)?
# What are the properties of numbers that create reversible sums?

# Things I notice as I play around:
# There are no reversible numbers between 100 and 200, or between 10000 and 100000
# Every four-digit sum is either symmetrical or 1000 + a symmetrical three-digit number
# Every sum has an even number of digits and is (after four digits) symmetrical


# Perhaps just adding up all even-number-of-entirely-odd-digits, symmetrical numbers 
# will just give us the answer? Seems likely that we hit every combination at some point

# We can go up to ten digits with our sums
# So we need to find the number of all-odd numbers for 1 through 5 digits
# (We can never get 11, can we ever get 1111 or 111111?)

# We could also create all possible sums and then "check them off" as we hit them, to get a better understanding of these patterns

# (There's probably some simple math I could do that would prove an answer easily, need to spend a bit more time thinking about the math
# that generates the results I've seen...)