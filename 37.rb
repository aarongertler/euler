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

i = 5           # Keeps our place as we move through the prime array (remember that this isn't the starting number -- it's the starting index)
t_primes = []   # The number of truncatable primes we've found so far

until t_primes.length == 11
  i += 1
  str = prime_array[i].to_s
  len = str.length
  if str[1..-1] =~ exclude_numbers then  # If any number but the first is even or 5, the truncated string can't always be prime
    puts str
    prime_array[i] = 0
  end
  store_str = str      # Store the original string so we can start over after we've truncated from the right (maybe there's a smoother way to do this?)
  for j in (1...len)
    str = str[1..-1]  # Truncate the string once (from the left)
    if !Prime.prime?(str.to_i) then
      prime_array[i] = 0  # The original prime doesn't work, wipe it out of the array
      break # Once we find a bad rotation, stop rotating, we're done with this number
    end
  end
  num = store_str.to_i # Just keep the prime as a number, since we'll be using mods to truncate from the right
  for k in (1...len)
    num = (num/10).floor  # Truncate the string once (from the right) (might be faster than truncating by array?)
    if !Prime.prime?(num) then
      prime_array[i] = 0  # The original prime doesn't work, wipe it out of the array
      break # Once we find a bad rotation, stop rotating, we're done with this number
    end
  end
  t_primes << prime_array[i] if prime_array[i] != 0
end

puts "Array: #{t_primes}"
puts t_primes.inject(0, :+)


# Ways to make this faster: 