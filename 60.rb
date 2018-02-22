# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order 
# the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. 
# The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.


# Ways to go about this:

# Try finding pairs of primes that work, saving them? Any working five-set will have two working pairs that also work with each other
# 	And you can check for groups of 3 very easily with this method: if a-b, and a-c, just check if b-c, and then you have a-b-c


require 'prime'

$prime_array = Prime.take_while {|p| p < 100 } # We'll keep testing upper limits until we hit the right answer

def digits n 
	Math.log10(n).to_i + 1
end

def concatenate n1, n2 # Is this faster than just concatenating strings and converting back to an integer? Something to test later
	n1 * (10 ** digits(n2)) + n2
end

# def concatenate n1, n2
# 	(n1.to_s + n2.to_s).to_i
# end

def create_set primes, start # Pass in an array of 1-5 primes
	if primes.length == 5
		return primes
	end
	i = 0
	$prime_array[start,$prime_array.length - 1].each do |i| # Only test primes we haven't checked yet
		puts "Now checking #{i}"
		if primes.all? { |x| Prime.prime?(concatenate(x, i)) && Prime.prime?(concatenate(i, x))}
			puts "#{i} works with #{primes}"
			primes << i
			return create_set(primes, $prime_array.index(primes.last) + 1) # Needed a "return" statement here, otherwise it would stop at the working number, run a futile create_set loop, then come back to where it left off and run again
		end
	end
end

# $prime_array.each do |i|
# 	value = create_set([i])
# 	if value != false
# 		puts "The final set of primes: #{value}"
# 		exit
# 	end
# end

puts create_set([13], 0)
# puts Prime.prime?(concatenate(13, 5197)) && Prime.prime?(concatenate(5197, 13))



# Initial problem: We were getting "stuck" with certain prime combinations
# For example, we'd have 13 and 19 and would then miss something like 5197 (which should've worked)

# puts create_set([3391,3433,3643,6607]) # Testing some promising 4-sets, but nothing works with primes up to 100000
# puts create_set([1283,1619,4127,7949])
# puts create_set([467,587,617,6323])
# puts create_set([11,23,743,1871])
# puts create_set([23,47,1481,4211])
# puts create_set([43,97,1381,8521])
# puts create_set([89,107,1061,4973])







