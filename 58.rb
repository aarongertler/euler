# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49

# It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting 
# is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

# If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. 
# If this process is continued, what is the side length of the square spiral for which the ratio of primes 
# along both diagonals first falls below 10%?

require 'prime'

layer = 2 # Start after the second "layer" has been applied 
diagonal = 9
primes = 3
non_primes = 2

until primes < (non_primes.to_f / 9) # Was dumb and tried to check for primes being less than 10% the number of *primes*, not less than 10% of the total
	4.times do
		diagonal = diagonal += 2*layer
		if Prime.prime?(diagonal)
			primes += 1
		else
			non_primes += 1
		end
	end
	layer += 1
end

puts "Primes: #{primes}, Non-Primes: #{non_primes}"
puts "Layer count: #{layer}"

# Holy cow, this took 9 seconds to calculate, and I'm only running math and primality checks! It's not even that many operations...
# Could increase speed by moving outside the default Ruby primality algorithm and using something like Miller-Rabin