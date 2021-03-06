
# An irrational decimal fraction is created by concatenating the positive integers:

# 0.123456789101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part, find the value of the following expression.

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

require 'benchmark'

# The big question: Can Ruby handle a million-character string?

string = "1"
count = 1
digits = 1
product = 1

puts Benchmark.measure {
	while digits < 10000000
	  count += 1
	  string << count.to_s # << is MUCH faster than += for strings
	  digits += count.to_s.length
	end

	product = 1

	for i in (0..7)
	  product = product * string[(10 ** i) - 1].to_i
	end
}

puts product # takes half a second

# Bonus two-line Ruby solution (which is, alas, much slower):

# string = (1..10000000).to_a.join('')
# puts 0.upto(7).reduce(1) { |memo, n| memo * string[10 ** n - 1].to_i }


# Ways to make this faster:
# 1. Find a formula for the nth digit (involves using a formula to find the index of the number n,
# which is actually pretty simple if n is a power of 10)

# Also, we know that there are 9 digits from 1-9, 180 digits from 10-99, 2700 from 100-999, etc.
# So that can help us with the indexing as well 