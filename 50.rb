# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one hundred.

# The longest sum of consecutive primes below one thousand that adds to a prime, 
# contains 21 terms, and is equal to 953.

# Which prime, below one million, can be written as the sum of the most consecutive primes?


# We know that the prime in question must be the sum of at least 22 consecutive primes
# And must be the sum of, at most, as many primes as it takes from 2...x before the sum exceeds one million

# Brute-force way: Add all prime numbers starting with "start" (the first prime in the sequence)
# Every time the sum is prime, record the number of consecutive primes you've added (if the streak is the longest streak you've seen so far)
# Keep choosing new start values and finding the longest consecutive sequences you can, until the start value is too high to work
# (Because any sufficiently long streak at that point would add up to more than a million)

require 'prime'

prime_array = Prime.take_while {|p| p < 50000 } # If we're adding 22 primes over 50000, our number will be over a million

longest_streak = 0 # The most consecutive primes we've been able to put together

for start in (0..100) # Starting with small initial values to see if we get a working answer (to get a long range, starting index is probably low anyway)
  i = start # The index of the first prime number in our sequence
  n = 0
  while n < 1000000
    streak = i - start
    if streak > longest_streak && Prime.prime?(n) # If we've gone far enough to break our record streak and see a prime number, record our new record!
      longest_streak = streak # Set number of consecutive primes = number of primes between our current and starting indicies if we've hit our longest streak ever
      sum = n
      range = [prime_array[start], prime_array[i]]
    end
    n += prime_array[i]
    i += 1
  end
end

puts longest_streak
puts sum
print range

# Fast enough that boosting speed isn't a huge concern, but there are some interesting Ruby solutions in the Euler thread