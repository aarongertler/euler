# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n 
# exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

# What is the largest n-digit pandigital prime that exists?


# Largest possible prime would be 9 digits. But is that possible?
# No, because sum of 1 to 9 is 45, so any 9-digit pandigital number is divisible by 3
# Similarly, sum of 1 to 8 is 36, so any 8-digit pandigital number is divisible by 3

# Is a 7-digit pandigital prime possible? I don't see why not.

# Is it faster to check all primes for pandigitality, or to check all pandigitals for primality?

# First, let's try the "check all 7-digit panditigals for primality" plan

require 'prime'

def permutation(string)
  return [''] if string.empty?

  (0...string.size).flat_map { |i|    # flat_map = "return all of our results in one array" (all the permutations)
    chr, rest = string[i], string[0...i] + string[i+1..-1]    # chr = letter we start with
    permutation(rest).map { |sub|
      chr + sub
    }
  }
end

all_permutations = permutation('1234567') # Returns an array of just 5040 numbers to check, hopefully this will be quick
# puts all_permutations

highest = 0

for i in (0...all_permutations.length)
  this_prime = all_permutations[i].to_i
  if Prime.prime?(this_prime)      # Our permutation array is already sorted least -> greatest, so the last prime will be the largest
    highest = this_prime
  end
end

puts highest
