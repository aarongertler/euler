# Euler's Totient function, φ(n) [sometimes called the phi function],
# is used to determine the number of positive numbers less than or 
# equal to n which are relatively prime to n. 

# For example, as 1, 2, 4, 5, 7, and 8, are all less than nine 
# and relatively prime to nine, φ(9)=6.

# The number 1 is considered to be relatively prime to every 
# positive number, so φ(1)=1.

# Interestingly, φ(87109)=79180, and it can be seen that 
# 87109 is a permutation of 79180.

# Find the value of n, 1 < n < 10^7, for which φ(n) 
# is a permutation of n and the ratio n/φ(n) produces a minimum.


# I feel like the solution to 72 ought to be useful here, since it gives us a quick way of finding totient counts.

def totient_table(limit):
	table = list(range(limit + 1)) # Will store the number of relatively prime numbers below each value of n (which equals n - phi(n))
	
	for n in range(2, limit + 1):
		if table[n] == n: # Don't use a number to cut unless it's prime (since cutting with 2 and 4 would be redundant)
			for k in range(n, limit + 1, n): # For every multiple of n, remove the number of fractions that are reducible (5 gets cut by 5 // 5 because 5/5 is removed, 10 gets cut by 10 // 5 because 5/10 and 10/10 are removed...)
				table[k] -= table[k] // n

	return table

# print(totient_table(10))

def digit_sort(x):
	x = str(x)
	return sorted(x)

limit = 10**7
min_dividend = 10
min_n = 0

answer_table = totient_table(limit)

for n in range(2, limit):
	if digit_sort(answer_table[n]) == digit_sort(n):
		new_dividend = n / answer_table[n]
		# print(n, "is a permutation, and the dividend is:", n / answer_table[n]) # Wow, there are a lot of these
		if new_dividend < min_dividend:
			min_dividend = new_dividend
			min_n = n

print("n that produces a minimum:", min_n) # Takes 30 seconds or so, but we get the right answer


# Way to make this faster: As with 69, think about the types of numbers that produce large numbers of relative primes
# These numbers won't be prime, because phi(n) for any prime number is just n - 1, and n - 1 can't be a permutation of n
# But we could just multiply two prime numbers together, which is the next-best thing
# And trying a reasonable range of primes (say, from 1,000 to 10,000) will only give us a few thousand multiples to check
# And then we just find the minimum dividend from a permutation

# Oh, and of course, we'll need phi(a * b), which is just (a - 1)*(b - 1), or ab - a - b - 1 + 2
# We subtract the 1 because we don't count ab itself
# We subtract a and b, then add 2, because there will be (a - 1) multiples of b below ab and (b - 1) multiples of a below ab
# For example, phi (3 * 7) = 2 * 6 = 12, all numbers but (3, 6, 9, 12, 15, 18), (7, 14), and 21 itself


