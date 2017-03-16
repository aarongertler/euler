# The number, 197, is called a circular prime because all rotations of the digits: 
# 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?


# First, initialize all primes below 1 million

require 'prime'

prime_array = Prime.take_while {|p| p < 1000000 } # Takes about a second to create this array (all primes under one million)

last = prime_array.length

exclude_numbers = /0|2|4|5|6|8/

for i in (0...last)
  str = prime_array[i].to_s
  if str.length > 1 && str =~ exclude_numbers then  # Any non-single-digit prime containing an even digit or 5 can't have prime rotations
    prime_array[i] = 0
    next
  end
  for j in (0...str.length)
    str = (str[1..-1] + str[0]).to_i  # Rotate the string once
    if !Prime.prime?(str) then
      prime_array[i] = 0  # The original prime doesn't work, wipe it out of the array
      break # Once we find a bad rotation, stop rotating, we're done with this number
    end
    str = str.to_s
  end
end

prime_array.reject! { |n| n < 1} # Get rid of all the zeroes (so we only have primes that work)
puts prime_array


# Ways to make this faster: Cut off all rotations you test as you go
# (so that you don't check 971 after checking 179)

