# There are exactly ten ways of selecting three from five, 12345:

# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

# In combinatorics, we use the notation, 5C3 = 10.

# It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

# How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?


# Formula to use: nCr = n! / r!(n-r)!

def factorial n 
	result = 1
	while n > 1
		result *= n
		n -= 1
	end
	result
end

# Let's just cache the factorials ahead of time

$factorials = [1] # Maybe a bit "un-Ruby", but for a script this small, I'm not bothered by the global variable

for i in (1..100)
	$factorials[i] = factorial(i)
end

puts factorial(5)
puts $factorials[5]

def n_choose_r n, r 
	# puts "Testing #{n} choose #{r}"
	$factorials[n] / ($factorials[r] * $factorials[n-r])
end

values = 0

for i in (23..100)
	for j in (4..100) # 100 choose 3 is less than 1 million, so 4 is the smallest value we need to check
		if n_choose_r(i,j) > 1000000
			values += 1
		end
	end
end

puts "Number of values: #{values}"

# Ways to make this faster: Use Pascal's Triangle to build up an array of n_choose_r values, rather than calculating everything from scratch