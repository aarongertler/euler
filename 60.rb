# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order 
# the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. 
# The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.


# Ways to go about this:

# Try finding pairs of primes that work, saving them? Any working five-set will have two working pairs that also work with each other
# 	And you can check for groups of 3 very easily with this method: if a-b, and a-c, just check if b-c, and then you have a-b-c


require 'prime'

$prime_array = Prime.take_while {|p| p < 10000 } # We'll keep testing upper limits until we hit the right answer

def digits n 
	Math.log10(n).to_i + 1
end

def concatenate n1, n2 # Is this faster than just concatenating strings and converting back to an integer? Something to test later
	n1 * (10 ** digits(n2)) + n2
end

# def concatenate n1, n2
# 	(n1.to_s + n2.to_s).to_i
# end

def create_set primes, next_prime # Pass in an array of 1-5 primes
	if primes.length == 5 # For now, we'll return the first set of five primes we find and assume that the sum will be lowest that way
		return primes
	end
	i = 0
	$prime_array.each do |i| # Only test primes we haven't checked yet
		if i > next_prime
			if primes.all? { |x| Prime.prime?(concatenate(x, i)) && Prime.prime?(concatenate(i, x))}
				# puts "#{i} works with #{primes}"
				primes << i
				return create_set(primes, primes.last) # Needed a "return" statement here, otherwise it would stop at the working number, run a futile create_set loop, then come back to where it left off and run again
			end
		end
	end
	unless primes.length == 1
		return create_set(primes - [primes.last], primes.last) # If the last set of primes didn't have a solution, remove the most recent prime you added and keep going with the previous numbers
	end
	false
end

$prime_array.each do |i|
	value = create_set([i], i)
	if value != false
		puts "The final set of primes: #{value}" # Pops out the answer in about 11 seconds, which (considering the slowness of other people's algorithms) I will accept
		exit
	end
end



# Initial problem: We were getting "stuck" with certain prime combinations
# For example, we'd have 13 and 19 and would then miss something like 5197 (which should've worked)
# The use of a "start" variable in the create_set function fixed this


# Ways to make this faster: 
# 1) Somehow skip pairs of primes that we've already checked and found to not work (this seems like more trouble than it would be worth)
