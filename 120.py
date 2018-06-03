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

# for i in range(1, 50):
	# print(remainder(7, i), i) # First fourteen numbers repeat (max at 3, r = 42)
	# print(remainder(6, i), i) # First six numbers repeat (max at 5, r = 24)
	# print(remainder(5, i)) # First 10 numbers repeat (max at 7, r = 20)
	# print(remainder(50, i), i) # (max at 49, r = 2400)
	# print(remainder(500, i), "n =", i) # (max at 249)


# So every number does seem to hit a natural limit. But what is that limit?

# Every even value of n returns a remainder of 2 (1^2 + (-1)^2)

# Odd values of n are more interesting. They run their course and go "back to zero"
# at some multiple of half the a value (e.g. 1249 gives a local maximum for a = 500, as does 2499)

# But it's an imperfect system, since it doesn't quite work for 5
# What I do notice is that the max reminders are almost equal to a^2: (a-1)*a for odds, (a-2)*a for evens
# Let's give that pattern a shot... (it's late, I don't feel like working out lots of polynomials at the moment)

r = 0
for a in range(3, 1001):
	if a % 2 == 0:
		r += (a-2)*a
	else:
		r += (a-1)*a

print(r) # Works! At least the code isn't brute-force, even if my reasoning was...
