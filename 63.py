# The 5-digit number, 16807=7^5, is also a fifth power. 
# Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

# How many n-digit positive integers exist which are also an nth power?


# How can we put an upper bound on this? 
# 2 has too few digits by 2^2
# 3: 3^2, 4: 4^3, 5: 5^4, 6: 6^5, 7: 7^7, 8: 8^11, 9: 9^22 (just checked these in Google's calculator)

# And then, once we get to 10, it never works, because there are always more digits than the power

# So we just build a simple function, no need to worry about stretching on to infinity

sum = 0

for i in range(1, 10): # Remember 1^1!
	n = 0
	digits = 1
	while digits >= n:
		n += 1
		digits = len(str(i**n))
		# print(str(i**n))
		# print("n:", n, "digits:", digits)
		if digits == n:
			sum += 1

print(sum)


# Even shorter solutions can use a formula to check digit count:
# digits = int(log10n) + 1
# We run out of digits when n^(x+1) < 10^x (since 10^x is the smallest x+1-digit number)
# int(1 / 1 - log10n) = power we can reach before running out of digits (not sure where this rule comes from, haven't found a proof)

# For example, log10(9^21) is just over 20, log10(9^22) is just under 21