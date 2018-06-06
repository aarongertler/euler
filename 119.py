# The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 8^3 = 512. 
# Another example of a number with this property is 614656 = 28^4.

# We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have a sum.

# You are given that a2 = 512 and a10 = 614656.

# Find a30.


# Strategy: Anything better than brute-forcing?
# If an odd number has an even digit sum, or an even number has an odd digit sum, it can't possibly work

def digit_sum(n): # Checked Stack Overflow, this method seems to be quickest
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def interesting(n):
	s = digit_sum(n)
	if (s % 2) != (n % 2):
		return False
	else:
		while s < n:
			s *= s
			if s == n:
				return True
	return False

start = 614656

print(interesting(614656))

