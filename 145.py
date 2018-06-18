# Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. 
# For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. 
# Leading zeroes are not allowed in either n or reverse(n).

# There are 120 reversible numbers below one-thousand.

# How many reversible numbers are there below one-billion (10^9)?


# ...this feels like it should be brute-forceable? (Maybe we can find a quick way to knock out half our numbers for a bit of bonus speed.)

# import math

# def get_digit(n, d): # https://stackoverflow.com/questions/39644638/how-to-take-the-nth-digit-of-a-number-in-python
# 	return n // 10**d % 10

# def reversible(n):
# 	if n % 10 == 0: # no leading zeroes!
# 		return False
# 	rev = int(str(n)[::-1])
# 	s = n + rev
# 	l = len(str(s))
# 	for d in range(0, l):
# 		if get_digit(s, d) % 2 == 0:
# 			return False
# 	# print(n, "is reversible, the reverse is", rev, "and the sum is", s)
# 	return True

# # print(reversible(409))
# # print(reversible(408))

# lower = 0
# limit = 10**7 # Brute force becomes impractical right around one million
# count = 0

# for i in range(lower, limit):
# 	if reversible(i):
# 		count += 1

# print(count)


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
# (We can never get 11, can we ever get 1111 or 111111?) (Yes, 902 + 209)

# We could also create all possible sums and then "check them off" as we hit them, to get a better understanding of these patterns

# Ways we can limit the numbers we check:
# Any number with first + last even or first + last odd digits won't work
# Any number with first + last digits >= 5 won't work
# ...but this feels rather dreary, and not an Euler-y way to do the problem

# (There's probably some simple math I could do that would prove an answer easily, need to spend a bit more time thinking about the math
# that generates the results I've seen...)

# Can we just cheat, and look at patterns for the number of numbers generally?

# 10^2 = 20   (20 * 1)
# 10^3 = 120 (+100) (20 * 6) (add 20 * 5)
# 10^4 = 720 (+600) (20 * 36) (add 20 * 30)
# 10^5 = 720
# 10^6 = 18720 (+18000) (20 * 936) (add 20 * 30 * 30)
# 10^7 = 68720 (+50000) (20 * 3436) (add 20 * 5 * 500)

# There's a hint of a pattern here, with 30 being a common factor in 10^4 and 10^6
# What if we try to extend that pattern?

limit = 9
total = 0

for d in range(2, limit + 1):
	if d % 2 == 0:
		total += 20 * (30 ** (d/2 - 1))
	if d % 4 == 3:
		total += 100 * (500 ** ((d + 1)/4 - 1))
	print(total)

# And... the derpy pattern just works. Curious to see other solutions...

# Looks like everyone's on brute force, but it's not too hard to see the reasons that only checking up to 10^8 is fine,
# you can rule out any possible 9-digit reversibles for the same reason you can rule out 5-digit reversibles.
# Take something likely-sounding like 14014: Doesn't work, because it produces 55055
# What if we want to carry a sum into the middle digit? Let's try 38038...
# ...and we hit 6 digits, so that doesn't work.
# How about 18052? You may see the issue by now. If we want to carry a number into the middle digit (so that the middle digit of our sum
# isn't just itself doubled, therefore even), we need the second and fourth digit to add to something that carries over...
# ...but then we're also carrying over into the first digit of the sum, as well as the third digit.
# If we carry over into the first digit, we need the first digit to have been even before, but that would mean the last digit is also even. It's a paradox -- we can't set things
# up so that we fix *all* of our even numbers at once. The same principle should apply to 9 digits, and 13 (but not 3 or 7).