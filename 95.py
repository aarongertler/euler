# The proper divisors of a number are all the divisors excluding the number itself. 
# For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. 
# As the sum of these divisors is equal to 28, we call it a perfect number.

# Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper 
# divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 
# are called an amicable pair.

# Perhaps less well known are longer chains. For example, starting with 12496, 
# we form a chain of five numbers:

# 12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

# Since this chain returns to its starting point, it is called an amicable chain.

# Find the smallest member of the longest amicable chain with no element exceeding one million.


# Very similar to problem 74, so I'll borrow some architecture.

from math import sqrt

limit = 1000000

# Find all the divisor sums (algorithm inspired by others' solutions to problems like this one, especially Dreamshire)

all_divs = [1] * limit # Everything is divisible by 1
for i in range(2, limit // 2): # Get the floordiv, just in case we test an odd limit at some point
	for j in range(2*i, limit, i): # Every time we choose a divisor i, we add that divisor to the divisor-sum for every number it can divide. If i were 7, for example, we'd add 7 to the divisor-sum for 14, 21, 28...
		all_divs[j] += i # All we care about is the sum of the divisors, not the divisors themselves

# print(all_divs[0:20])

# Got stuck earlier because I forgot to set us to stop when we looped back to the original number;
# instead, I was counting chains that wound down to 1

def chain(n):
	# print("Checking n =", n)
	terms = []
	while n < limit:
		n = all_divs[n]
		if n in terms:
			return len(terms) - terms.index(n), min(terms[terms.index(n):]), terms
		else:
			terms.append(n)
	return(0, 0, 0) # Didn't form a chain, doesn't matter

# print(chain(138))
# print(chain(25))
# print(chain(12496)) # Returns (5, 12496), as intended

longest_chain = 0
smallest_member = 10**7

for n in range(1, limit):
	chain_n = chain(n)
	if chain_n[0] > longest_chain:
		print(chain(n))
		longest_chain = chain_n[0]
		smallest_member = chain_n[1]

print("Longest chain has a distance of", longest_chain, "and the smallest member is", smallest_member)

# Got a wrong answer for a bit because I hadn't realized we needed something inside the chain, rather than the number that started the chain being eligible.