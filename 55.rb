# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

# Not all numbers produce palindromes so quickly. For example,

# 349 + 943 = 1292,
# 1292 + 2921 = 4213
# 4213 + 3124 = 7337

# That is, 349 took three iterations to arrive at a palindrome.

# Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. 
# A number that never forms a palindrome through the reverse and add process is called a Lychrel number. 
# Due to the theoretical nature of these numbers, and for the purpose of this problem, 
# we shall assume that a number is Lychrel until proven otherwise. 
# In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, 
# or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. 
# In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome.

# Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

# How many Lychrel numbers are there below ten-thousand?


# For each number below 10,000:
# 1. Reverse it 
# 2. Add the reverse to itself
# 3. Repeat this process until we hit a palindrome or we've done this 50 times with no palindrome

def reverse n # I could do this mathetmatically, by recursively multiplying each digit (back-to-front) of our starting number by 10, but I'll keep the code short
	n.to_s.reverse.to_i
end

lychrels = 0

for i in 1..10000
	sum = i + reverse(i)
	iterations = 1
	until sum == reverse(sum) || iterations == 50
		sum += reverse(sum)
		iterations += 1
	end
	if iterations == 50
		lychrels += 1
	end
end

puts lychrels # Computes in a fraction of a second, not going to put effort into speeding this up
