# It is well known that if the square root of a natural number is not an integer, 
# then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

# The square root of two is 1.41421356237309504880..., 
# and the digital sum of the first one hundred decimal digits is 475.

# For the first one hundred natural numbers, find the total of the digital sums of the 
# first one hundred decimal digits for all the irrational square roots.


# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Digit-by-digit_calculation

# Lots of methods here; base 2 is cute, but we'll stick to a base 10 algorithm
# Thankfully, this should give us total precision, lots of methods on that page just give estimates

# def test(n):
# 	return n+1, n+2

# a, b = test(2)

# print(a, b)

from math import log10, sqrt


# c is reminder * 100

def next_digit(p, x, y, c):
	while (x + 1)*(20*p + x + 1) <= c:
		x += 1
	y = x*(20*p + x)
	c = c - y
	return x, y, c*100


def square_root(n, precision): # precision = number of decimal digits we want to find
	p, x, y, c = 0, 0, 0, n
	digits = []
	limit = precision + 2 # Don't count the digits before the decimal point (since we're only looking at the first 100 numbers, there will only be one digit) (added an extra digit to avoid rounding errors)
	while len(digits) < limit:
		x, y, c = next_digit(p, x, y, c)
		digits.append(x)
		x = 0
		p = int(''.join(str(x) for x in digits))
	return digits

def digit_sum(n, precision):
	return sum(square_root(n, precision)[0:-2]) # Chop off last digit, since we have an extra digit to avoid rounding errors
			# Also, Euler meant "significant digits", not "decimal digits", so you count the 1 in 1.414... (grumble)

print(square_root(2, 100))
# print(square_root(99, 100))
# print(digit_sum(2, 100)) # Problem says first 100 "decimal digits", but the sum they give includes the 1 in 1.414...

result = 0
digits = 100

for i in range(2,100): # ignore 1 and 100, they are perfect squares
	if sqrt(i) % 1 != 0: result += digit_sum(i, digits)

print(result) # This was wrong for a while before I realized Euler hadn't stated the problem correctly (see "decimal digits" comment, above), and that I was rounding wrongly before I added an extra digit of precision
	
# Also, Dreamshire just imported a module to find decimals. Heh.