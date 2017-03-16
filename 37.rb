# The number 3797 has an interesting property. 
# Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. 
# Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


# How do we know there are only eleven of these primes? What's the upper bound?
# Maybe finding the upper bound takes really advanced math, so they've given us the upper limit of eleven?
# I guess I'll start with brute force.

require 'prime'

prime_array = Prime.take_while {|p| p < 900000 } # Upper bound turns out to be 800000 or so

exclude_numbers = /0|2|4|5|6|8/

i = -1          # Keeps our place as we move through the prime array
t_primes = []   # The number of truncatable primes we've found so far

until t_primes.length == 11 || prime_array[i] == nil
  i += 1
  str = prime_array[i].to_s
  if str.length == 1 || str[1..-1] =~ exclude_numbers then  # If any number but the first is even or 5, the truncated string can't always be prime
    prime_array[i] = 0
    next
  end
  store_str = str      # Store the original string so we can start over after we've truncated from the right
  for j in (1...str.length)
    str = str[1..-1]  # Truncate the string once (from the left)
    if !Prime.prime?(str.to_i) then
      prime_array[i] = 0  # The original prime doesn't work, wipe it out of the array
      break # Once we find a bad rotation, stop rotating, we're done with this number
    end
  end
  str = store_str
  for k in (1...str.length)
    str = str[0...-1]  # Truncate the string once (from the right)
    if !Prime.prime?(str.to_i) then
      prime_array[i] = 0  # The original prime doesn't work, wipe it out of the array
      break # Once we find a bad rotation, stop rotating, we're done with this number
    end
  end
  t_primes << prime_array[i] if prime_array[i] != 0
end

puts "Array: #{t_primes}"
puts t_primes.inject(0, :+)


# Ways to make this faster: Lots, at least aroudn the edges
# A more efficient truncation algorithm might be the best idea -- try creating "left" and "right"
# arrays and adding each digit to those, so that you're checking isPrime for smaller rather than larger 
# numbers at the beginning

# Generating the initial array of primes might also be less efficient than checking each number for 
# prime-ness as we go -- not sure how many of these primes come preloaded in Ruby (but probably a lot)