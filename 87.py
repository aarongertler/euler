# The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. 
# In fact, there are exactly four numbers below fifty that can be expressed in such a way:

# 28 = 2^2 + 2^3 + 2^4
# 33 = 3^2 + 2^3 + 2^4
# 49 = 5^2 + 2^3 + 2^4
# 47 = 2^2 + 3^3 + 2^4

# How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?


# This shouldn't be too hard to brute-force. The highest number we'll want to check for each exponent is:

# For x^2, highest possible x is sqrt(50,000,000)
# For x^3, highest possible x is cube root of (50,000,000)
# For x^4, highest possible x is sqrt(sqrt(50,000,000))

# (But of course, we'll use only the primes below those values)

from sympy import primerange

limit = 50000000
numbers = set()

# def sqrt(a): # Didn't need these after all
# 	return int(a**0.5)

# def cube_root(a):
# 	return int(a**(1./3.))

# def fourth_root(a):
# 	return int(a**0.25)

primes = list(primerange(2, sqrt(limit)))

# print(len(primes)) # Just 908 primes we'll ever have to check, that's not too many

# Start the loop with our fourth roots, since those will add up fastest

for a in primes:
	for b in primes:
		if b**3 > limit - a**2:
			break
		for c in primes:
			if c**4 > limit - a**2 - b**3:
				break
			# print("Found triplet", a, b, c)
			numbers.add(a**2 + b**3 + c**4)

print(len(numbers)) # Solves in three seconds

# Ways to make this faster/more elegant:
# 1. Just setting a new limit on b and c based on the values of a and (a,b), respectively,
	# instead of checking an "if" statement every time, would be nice 
# 2. Create three different sets of primes corresponding to the square, cube, and fourth roots
	# of the limit, then loop over those different sets of primes (avoids ugly "break" functions)
# 3. Consider using itertools to build your nested loop, as Dreamshire did:
	# for a,b,c in product(sieve(7072), sieve(369), sieve(85)):



