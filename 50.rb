# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one hundred.

# The longest sum of consecutive primes below one thousand that adds to a prime, 
# contains 21 terms, and is equal to 953.

# Which prime, below one million, can be written as the sum of the most consecutive primes?


# We know that the prime in question must be the sum of at least 22 consecutive primes
# And must be the sum of, at most, as many primes as it takes from 2...x before the sum exceeds one million

require 'prime'

prime_array = Prime.take_while {|p| p < 100000 }

# i = 0
# sum = 0

# while sum < 1000000
#   sum += prime_array[i]
#   i += 1
# end

# puts sum - prime_array[i] # Alas, this number isn't prime
# puts i # 


# Brute-force way: Add all prime numbers starting with "start" (the first prime in the sequence)
# Every time the sum is prime, record the number of consecutive primes you've added (if the streak is the longest streak you've seen so far)
# Keep choosing new start values and finding the longest consecutive sequences you can, until the start value is too high to work
# (Because any sufficiently long streak at that point would add up to more than a million)

n = 0
i = 0
consecutive = 0
consecutive_n = 0

for start in (0..100)
  i = start # The index of the first prime number in our sequence
  n = 0
  while n < 1000000
    if i - start > consecutive && Prime.prime?(n)
      consecutive = i - start # Set number of consecutive primes equal to the number of primes between our current and starting index if we've hit our longest streak ever
      consecutive_n = n
      range = [prime_array[start], prime_array[i]]
    end
    n += prime_array[i]
    i += 1
  end
end

puts consecutive
puts consecutive_n
puts range
