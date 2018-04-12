# The first known prime found to exceed one million digits was discovered in 1999, 
# and is a Mersenne prime of the form 2^6972593−1; it contains exactly 2,098,960 digits. 

# Subsequently other Mersenne primes, of the form 2p−1, have been found which contain more digits.

# However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×2^7830457+1.

# Find the last ten digits of this prime number.


# There's a pattern of some kind happening here. Can we see it visually/

# limit = 100

# for i in range(limit - 20, limit):
# 	result = 2**i
# 	print(str(result)[-10:])

# Nothing obvious to the naked eye.

# We can avoid working with giant numbers and just store successive 10-digit numbers (since the last ten digits of a power of 2 only care about the last ten digits of the previous power of 2)
# The question is: Can we really process seven million of them at a reasonable pace?

# (Just in case, I checked on 2**7000000, took over 20 seconds to compute)

# print("Big number:", str(2**1000000)[-10:])

test_num = 80 # We can either start with a real power of 2, or just seed a high value to save a few seconds. I'm fine with seeding.
start = 2**test_num
count = test_num

count = 1000000
start = 2747109376 # Last 10 digits of 2^1000000 (NOTE: Might be somewhat off if Python handles very big numbers badly)

while count < 7830457: # As it turns out, this is easily fast enough
	result = int(start) # Needs to have "int" to avoid assigning two names to the same variable
	start = str(result*2)[-10:]
	count += 1

answer = str(28433*(int(start)) + 1)[-10:]

print("Answer:", answer) # Answer comes out in 5 seconds


# Ways to make this faster:
# 1. Well, this is easy. Python's pow() function apparently returns super-fast results if you use a modulus to keep the number of digits down.
	# This makes the solution instant.

# print(str(pow(2, 1000000, 10**10))[-10:])

