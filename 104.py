# The Fibonacci sequence is defined by the recurrence relation:

# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital 
# (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci number 
# for which the first nine digits are 1-9 pandigital.

# Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.

def is_pandigital(n):
	s = str(n)
	return ''.join(sorted(s)) == "123456789"

def first_pandigital(n):
	s = str(n)
	return ''.join(sorted(s[:9])) == "123456789"

# print(first_pandigital(1234567981234))

def fib_cycle(limit):
	n = 2
	a, b = 1, 1
	while n < limit:
		a, b = b, a+b
		n += 1
		if n > 100000: # Saving some time by removing loops we've worked through
			if is_pandigital(b % 10**9): # Get last 9 digits
				print("Checking a new number at n =", n)
				if first_pandigital(b):
					print("Answer:", n)
					break
	# print(b)

fib_cycle(350000) # There are a lot of fibonacci numbers with a pandigital last 9! Still, this comes in at just under a minute, with no fancy tricks needed to grab first 9 digits