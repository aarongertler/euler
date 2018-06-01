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

print(remainder(7, 3))
