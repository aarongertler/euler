# It is possible to write ten as the sum of primes in exactly five different ways:

# 7 + 3
# 5 + 5
# 5 + 3 + 2
# 3 + 3 + 2 + 2
# 2 + 2 + 2 + 2 + 2

# What is the first value which can be written as the sum of primes 
# in over five thousand different ways?


# We can't reuse #78 here, like we did for #76. At least, not completely.

# But Wolfram says this is a known result: http://mathworld.wolfram.com/PrimePartition.html
# Here's a sequence that lets us calculate the answer: http://oeis.org/A000607

# And here's a table where this can just be looked up... but I'll program it anyway
# http://chesswanks.com/seq/sopfr/

# prime_partitions(n) = 1/n * sum(k = 1..n) of factor_sum(k)*prime_partitions(n - k)
# Where factor_sum(k) = the sum of all the primes that distinctly divide k

# factor_sum(k) details on OEIS: http://oeis.org/A008472

# So I'll start by writing factor_sum

from math import sqrt

def prime_factors(n):
	factors = set()
	factor = 2
	while n > 1:
		while n % factor == 0:
			n /= factor
			factors.add(factor) # This means we'll technically add 2 multiple times, so it might be a tad slow, but I don't think we'll notice on the range of numbers we're using
		factor += 1
	return factors

def factor_sum(n):
	if n == 1: return 0
	return sum(prime_factors(n))

# print(prime_factors(45))
# print(factor_sum(45))

# prime_partitions(n) = 1/n * sum(k = 1..n) of factor_sum(k)*a(n - k)

prime_partitions = [1, 0, 1]

def prime_partition(n):
	answer = 0
	for k in range(1, n + 1):
		answer += factor_sum(k)*prime_partitions[n - k] # Consider building a collection of factor_sums to speed this up
	return answer/n


i = 2
p = 1

while p <= 5000:
	i += 1
	p = prime_partition(i)
	prime_partitions.append(p)

print(int(p))
print(i) # Surprisingly low!

# This returns an answer instantly, so I don't feel the need to speed it up.
# But I do wonder whether I'd have been able to derive this formula myself.

# My reasoning: Let's say we want to find prime_partitions(13).
# We want to see how many ways we could add two to each possibility from prime_partitions(11),
# since this is the same as building prime partitions of 13
# So there are prime_partitions(11) ways to build 13 by adding 2 to each of 11's partitions
# In other words, we've added factor_sum(2)*prime_partitions(13-2)
# What if we want to add prime partitions of 5 to prime partitions of 8?
# In that case, factor_sum(5) is 2, because we have (5) and (3,2)
# We can add either 5 OR 3 and 2 to any prime partition of 8, and get a working 13
# So we've added factor_sum(5) * prime_partitions(13-5).

# And so on. At the end, we divide by n as a way, I assume, of removing duplicates.
# After all, we'll have built 5-3-3-2 from 11 and 2, 10 and 3, and several other pairs
# Though I don't know why we'd have exactly enough duplicates that dividing by n gives us the right answer. Hm.


# Dreamshire has a more natural solution that breaks things down in the same way I did above
# And they also use dynamic programming! Similar to problem #31 as well.

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]

L, target = 5000, 5
# while True:
ways = [1] + [0]*target
for p in primes:
    for i in range(p, target+1):
        ways[i] += ways[i-p] # Each time we look at a new prime, we see how many ways it can help to fill in the numbers we're looking at.
        # For 5, we look when p = 2 (and find nothing, since we don't know about 3 yet)
        # We look when p = 3 (and hey, because we filled in 2 as a prime, we know that we can add 2 to 3, so 3 adds one solution to 5 when it looks at 5-3)
        # We also look when p = 5 (and we know that's prime, because i - p = 0, so we add one solution)
        # Because ways[0] = 1, we'll add one solution for every prime that is just (that prime)
        # And every time we look at a smaller prime that could fit into a bigger number, we add the number of ways to break down that prime
        # When we look at 10, we find that ways[10] += ways[7] and ways[5].
        # We can break 7 down three different ways, and add 3 to each of them
        # Or break 5 down two different ways, and add 5 to each of them
        # Only looking at 7 or 5 once ensures that we don't get duplicates (for example, trying 2,3,5 and 5,2,3)
# if ways[target] > L: break    
    # target += 1

print(ways)