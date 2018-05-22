# The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 
# 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.

# There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of these palindromes is 4164. 
# Note that 1 = 0^2 + 1^2 has not been included as this problem is concerned with the squares of positive integers.

# Find the sum of all the numbers less than 10^8 that are both palindromic and can be written as the sum of consecutive squares.


# The largest square we could possibly check would be 10^4
# Brute force would have us start with each square number and add from there, recording every palindrome we find...
# ...but that would be a lot of operations. How can we work more efficiently?

# (Starting with all the palindromic numbers feels like a dead end, since dissecting "sum of squares" from them is rough)

# Still, I'll start with brute force:

limit = 10**8
last_check = int(limit**0.5) # This number squared is already near the limit, so we'll never add to it

def palindrome(n):
	return str(n) == str(n)[::-1]

# print(palindrome(595))

# for i in range(1, last_check): # Is it more efficient to draw from an array of square numbers, or to square repeatedly as you go along?
# 	s = i**2
#		for j in range(i + 1, last_check): # Was making mistake of looking at whole range here, not stopping when we hit limit
# 		s += j**2
#			if s > limit: # Added this line to speed things up
#				break 
# 		if palindrome(s):
# 			print("Palindrome found:", s)
# 			total += s # would need to fix this to only grab unique palindromes, too

# print("Total:", total) # Works in theory, slow in practice

# Let's think about the mathematical properties of numbers that are the sum of consecutive squares:

# Starting at 1^2, we have 1, 5, 14, 30...
# Starting at 2^2, we have 4, 13, 29, 54...
# The formula starting at 1^2 is (n)(n + 1)(2n + 1) / 6
# If we think about the general case of starting at n, we have n^2 + (n + 1)^2 + (n + 2)^2 ... + (n + m)^2
# (Where m is the number of squares we look at beyond the first)
# Which comes out to n^2 + (n^2 + 2n + 1) + (n^2 + 4n + 4) ... + (n^2 + 2mn + m^2)
# Which is the same as n^2 + m*n^2 + m*(mn+n) + (m)(m+1)(2m+1)/6
# Second term: We add n^2 m times
# Third term: We have m terms in a series with average value (2mn + 2n)/2 (first + last / 2)
# Fourth term: Just the formula for adding 1^2 to m^2, see above

# Making sure this formula works...

def sum_of_squares(n, m):
	return n**2 + m*(n**2) + m*(m*n + n) + m*(m + 1)*(2*m + 1)/6

# print(sum_of_squares(6,6)) # Perfect! Gets us 595

palindromes = set()
count = 0
for i in range(1, last_check):
	for j in range(i + 1, last_check): # Add 1 to i so we take at least one "step"
		sos = int(sum_of_squares(i, j-i))
		if sos > limit:
			break
		if palindrome(sos):
			count += 1
			# print("Palindrome found:", sos, "Count:", count)
			palindromes.add(sos)

# print(sum(pals))
print(sum(palindromes)) # Finishes in one second! Just had to adjust for the "unique" palindrome instruction