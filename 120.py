# Let r be the remainder when (a−1)^n + (a+1)^n is divided by a^2.

# For example, if a = 7 and n = 3, then r = 42: 6^3 + 8^3 = 728 ≡ 42 mod 49. 
# And as n varies, so too will r, but for a = 7 it turns out that rmax = 42.

# For 3 ≤ a ≤ 1000, find ∑ rmax.


# We're finding the largest possible remainder for any a between 3 and 1000
# But there are no limits on n! Interesting. So it would seem that the remainder necessarily shrinks over time as n grows. Why?


def remainder(a, n):
	total = (a-1)**n + (a+1)**n
	rem = total % a**2
	return rem

for i in range(2400, 2510):
	# print(remainder(7, i)) # First fourteen numbers repeat
	# print(remainder(6, i)) # First six numbers repeat
	# print(remainder(5, i)) # First 10 numbers repeat
	# print(remainder(50, i)) # Highest remainder steadily increases
	# print(remainder(500, i), "n =", i) # Similar to 50, no apparent upper limit... until I start looking at values in the 1000 range


# So every number does seem to hit a natural limit. But what is that limit?

# Every even value of n returns a remainder of 2 (1^2 + (-1)^2)

# Odd values of n are more interesting. They run their course and go "back to zero"
# at some multiple of half our a value (e.g. 1249 gives a local maximum for a = 500, as does 2499)

# 


