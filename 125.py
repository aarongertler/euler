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
total = 0
last_check = int(limit**0.5) + 1 # Since this number squared is already very close to the total, it's the last number we'd ever need to add to any sum

# def palindrome(n):
# 	return str(n) == str(n)[::-1]

# # print(palindrome(595))

# for i in range(1, last_check): # Is it more efficient to draw from an array of square numbers, or to square repeatedly as you go along?
# 	s, numbers_added = 0, 0 # Record the sum as we go along, and note when we've actually added multiple numbers
# 	for j in range(i, last_check):
# 		s += j**2
# 		numbers_added += 1
# 		if palindrome(s) and s < limit and numbers_added > 1:
# 			print("Palindrome found:", s)
# 			total += s

# print("Total:", total) # Works in theory, much too slow in practice


# Let's think about the mathematical properties of numbers that are the sum of consecutive squares:

# Starting at 1^2, we have 1, 5, 14, 30...
# Starting at 2^2, we have 4, 13, 29, 54...
# The formula starting at 1^2 is (n)(n + 1)(2n + 1) / 6
# If we think about the general case of starting at n + 1, we have (n + 1)^2 + (n + 2)^2 ... + (n + m)^2
# Which comes out to n^2 + 2n + 1 + n^2 + 4n + 4 ... + n^2 + 2mn + m^2