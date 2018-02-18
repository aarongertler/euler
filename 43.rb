# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of 
# the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.


# There are 3.6 million possible permutations of the 10 digits
# Presumably, we can exclude the 0.36 million that start with 0 (but check this assumption if your answer is wrong)

# The sixth digit needs to be 5 or 0
# The fourth digit needs to be even
# There are only 53 ways the last three digits can be arranged (53 = 986 - 102 / 17 = the number of multiples of 17 in that range) 
# Build that into a permutation algorithm?

# def digit_permutation(string)
#   # return [''] if string.chars.sort.join == '123456789' # Don't sort if number would start with 0
#   # return [''] if string.length == 6 && string.include?('5') && string.include?('0')
#   return [''] if string.empty?

#   (0...string.size).flat_map { |i|    # flat_map = "return all of our results in one array" (all the permutations)
#     chr, rest = string[i], string[0...i] + string[i+1..-1]    # chr = letter we start with
#     digit_permutation(rest).map { |sub|
#       chr + sub
#     }
#   }
# end


# This permutation thing seems clumsy, though it would be an interesting exercise to build
# permutations with certain digits pre-defined. Let's do something else.

# Fancy procedure: Start with a given multiple of 17. Remove all digits in that multiple
# from an array of digits 1-10. If we still have 7 digits left, add the first one on the list.
# If the resulting three-digit number is divisible by 13, keep going. Otherwise, add the second
# of the 7 digits to our multiple of 17 and try again.

# This should actually cut short very quickly. Only 53 multiples of 17 to test, and most of them will be 
# cut off after the 13 check. Let's see if we can write out this monster...

$solutions = []

def digit_loop(digit_string, prime_index, digits) # Takes a multiple of 17 and checks each prime multiple if we find working digits to add
  prime_array = [13,11,7,5,3,2]
  prime = prime_array[prime_index]
  if digit_string.length == 9
    pandigital = digits[0] + digit_string
    puts "We found a solution: #{pandigital} for seed value #{digit_string[6..-1]}"
    $solutions << pandigital.to_i
  else
    for i in (0..digits.length - 1) # Had three periods, needed two
      digit_string = digits[i] + digit_string # Add next digit in front of existing digits to make a new number to test
      if digit_string[0..2].to_i % prime == 0 # Check whether the first three digits of the current number are divisible by the prime we're checking
        digit_loop(digit_string, prime_index + 1, (digits - [digits[i]])) # Every time we find a digit that "fits", we recur the loop through all possible combinations of other digits
      end
      digit_string = digit_string[1..-1] # Remove the digit we tried if it didn't work, try the next digit insteads
    end
  end
end

count = 5

until count * 17 > 1000    # Seed our test pandigitals with multiples of 17
  digit_array = ["0","1","2","3","4","5","6","7","8","9"]
  count += 1
  string = (count * 17).to_s
  for i in (0..2)   # Remove digits we used in our multiple of 17
    digit_array = digit_array - [string[i]]
  end
  if digit_array.length == 7
    digit_loop(string, 0, digit_array) # Our multiple of 17 has no duplicates! Let's see if we can use it to build a pandigital
  end
end

puts $solutions.inject(0, :+)


# Other options: Just use brute force (but I think this recursive solution is prettier, even if it may be a bit slower? Uncertain)


# Using a bunch of each_do lists might be a bit more efficient, as with this elegant solution:

# d_17s = []
# (17..999).each do |i|
#   if i % 17 == 0
#     to_push = i.to_s
#     to_push.prepend('0') if to_push.length < 3
#     d_17s << to_push
#   end
# end

# to_do_list = d_17s
# len = 4
# [13, 11, 7, 5, 3, 2].each do |p|
#   tmp_list = [] # Aaron's note: Once we find working multiplew of 13 for a 17 base, we add it here and try 11, and so on
#   to_do_list.each do |n|
#     (0..9).each do |o|
#       if (o.to_s + n[0..1]).to_i % p == 0
#         push_data = o.to_s + n[0..-1]
#         tmp_list << push_data  if push_data.chars.uniq.count == len
#       end
#     end
#   end
#   len += 1
#   to_do_list = tmp_list  # Aaron's note: Take all the working numbers we've found so far, then make them "todos" to test with the other primes
# end

# sum = 0

# # This is to find the first digit and then sum them
# to_do_list.each do |ans|
#   sum += (ans.prepend(('1234567890'.chars - ans.chars).join(''))).to_i
# end

# puts sum