# First new Euler I've solved in almost a year, and this may be the ugliest code I've ever written in any language.
# Still runs pretty fast, though, and there's a much more elegant solution (without so much array back-and-forth)
# available here for anyone interested: http://www.mathblog.dk/project-euler-51-eight-prime-family/



# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values, 
# 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes 
# among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. 
# Consequently 56003, being the first member of this family, is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, 
# is part of an eight prime value family.


# 1) List a bunch of primes (start with everything under 1 million)
# 2) For each prime, convert it to an array of digits, then gather a set of "places to look" that we can replace with the single digit of our choice 
# 2a) Start with combinations of two digits, then three, then four


# Assumptions I'm making for now:

# Single digit: We're taking a prime and adding 1 to it (can't do this enough times to get eight primes, since multiples of 3 interfere)
# 	So we need to change at least two digits
# 	But if we change two digits, we'll hit a multiple of three
# 	So we actually need to change at least three digits, since that way we increase the sum of digits by three each time (and avoid multiples of three)
# 		For the same reason, we can't change four digits... so we only need to change three (or six) digits
# We can't change the last digit, or we'll get even numbers
# Whatever prime we've chosen must not have digits adding to a multiple of three (once we've taken out our key digits)
# ALSO, whatever the lowest prime is, the repeated digits must be 0, 1, or 2 (or it won't be the lowest prime)

require 'prime'

digits = [0,1,2,3,4,5,6,7,8,9]

prime_array = Prime.take_while { |p| p < 1000000 } # Primes should be at least four digits if we're changing three digits

prime_digit_array = prime_array.map { |i| 
	i = i.to_s
	i.each_char.map(&:to_i) # Convert each character in our string to a separate integer/digit in our array of arrays
}

three_instance_primes = [] # A list of all primes that have at least three repeating digits (eliminating some primes from consideration)

prime_digit_array.each do |prime|
	for i in (0..2) # Only check the digits 0, 1, and 2 (if we're trying to find the lowest prime)
		if prime[0..prime.length - 2].count(i) > 2 # Only check the non-final digits of these primes
			three_instance_primes << prime
		end
	end
end

# If we're replacing at three indices for each prime number, only certain combinations of indices matter:
# 	For a four-digit number n, we can only replace n[0], n[1], and n[2] ([0,1,2])
# 	For a five-digit number, we can replace [0,1,2], [0,1,3], [0,2,3], and [1,2,3]
#   ...and so on. We could manually generate these lists of replacement indices, but we could also:
# 		1) Create all permutations of the right indices, 2) Trim a digit or two from the front of each permutation, and 3) Keep only unique results

# For the sake of readability, we'll start by doing the manual thing:

five_digit_patterns = [
	[0,1,2],
	[0,1,3],
	[0,2,3],
	[1,2,3]]

six_digit_patterns = [
	[0,1,2],
	[0,1,3],
	[0,1,4],
	[0,2,3],
	[0,2,4],
	[0,3,4],
	[1,2,3],
	[1,2,4],
	[1,3,4],
	[2,3,4]]

def replace array, pattern, digit # Replace the digits in the starting number array with the specified digit, using a replacement pattern
	if array[pattern[0]] != array[pattern[1]] || array[pattern[0]] != array[pattern[2]]
		return [0] # Make sure we're only replacing digits that are the same (instead of, say, replacing the first three digits of 100109)
	end
	if pattern[0] == 0 && digit == 0 # No leading zeroes allowed! (this messed me up earlier)
		return [0]
	end
	test_array = array.dup # This was necessary so that our changed arrays wouldn't keep getting tested
	pattern.each do |i|
		test_array[i] = digit
	end
	test_array
end

def array_to_integer array
	array.inject{|n, d| n * 10 + d}
end

def family_size number, pattern
	size = 0
	for i in (0..9)
		integer_prime = array_to_integer(replace(number, pattern, i))
		if Prime.prime?(integer_prime)
			size += 1
		end
	end
	size
end

# print family_size([1,0,0,1,0,9], [1,2,4])

three_instance_primes.each do |n|
	if n.length == 5
		# puts "Checking #{n}"
		five_digit_patterns.each do |pattern|
			# puts "Checking #{n}"
			if family_size(n, pattern) > 7
				puts "Answer found! It's #{n}"
			end
		end
	elsif n.length == 6
		six_digit_patterns.each do |pattern|
			# puts "Checking #{n}"
			if family_size(n, pattern) == 8
				puts "Answer found! It's #{n}"
				puts "Family size of #{n} is #{family_size(n, pattern)} with #{pattern}}"
				exit
			end
		end
	end
end

# NOTE: It seems like 111109 should work, as it is a prime number with a family size of 8, but I was missing the fact that
# my algorithm counted 000109 as an option (leading zeroes aren't allowed)




# SCATTERED NOTES THAT DIDN'T HELP MUCH:

# Never mind the above, I think I found a faster way. Let's go with process of elimination:
# 1) Look at a list of prime numbers and choose any that have at least three instances of the same digit

# three_instance_primes = []

# prime_digit_array.each do |prime|
# 	for i in (0..2) # Only check the digits 0, 1, and 2 (if we're trying to find the lowest prime)
# 		if prime[0..prime.length - 2].count(i) > 2 # Only check the non-final digits of these primes
# 			three_instance_primes << prime
# 		end
# 	end
# end

# three_instance_primes = three_instance_primes.uniq # Don't add something like 1001011 twice

# print three_instance_primes # Boy, there are a lot of these

# 2) Replace each instance of the repeating digit with a "0" for each number (risky, yes, since we'll butcher numbers with *four* instances,
# but it's at least a starting point) (edit: No, we didn't get any useful results out of this)

# three_instance_primes.each do |prime|
# 	for i in (0..9)
# 		if prime[0..prime.length - 2].count(i) > 2 # Only check the non-final digits of these primes
# 			prime.map! { |x| x == i ? 0 : x }
# 		end
# 	end
# end

# # print three_instance_primes

# freq = three_instance_primes.inject(Hash.new(0)) { |h,v| h[v] += 1; h }

# print freq.sort_by { |prime,freq| freq } # This gives us a set of 40 or so digit combinations that appear frequently

