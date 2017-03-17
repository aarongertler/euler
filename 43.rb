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
# Presumably, we can exclude the 0.36 million exclude_numbers = /0|2|4|5|6|8/that start with 0 (but check this assumption if your answer is wrong)

# The sixth digit needs to be 5 or 0
# The fourth digit needs to be even
# There are only 53 ways the last three digits can be arranged (986 - 102 / 17)
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

$solutions = []   # Declaring a global feels wrong, but it's a shortcut to knock this one out for now 

def digit_loop(digit_string, prime_index, array)
  prime_array = [17,13,11,7,5,3,2]
  prime = prime_array[prime_index]
  if digit_string.length == 9
    puts "We found a solution: #{array[0] + digit_string} for seed value #{digit_string[6..-1]}"
    $solutions << (array[0] + digit_string).to_i
  else
    for i in (0...array.length)
      if i == array.length then  # For some reason, i was looping too far
        break
      end
      digit_string = array[i] + digit_string # Add next digit in front of array
      if digit_string[0..2].to_i % prime == 0
        digit_loop(digit_string, prime_index + 1, (array - [array[i]]))
      end
      digit_string = digit_string[1..-1]
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
    digit_loop(string, 1, digit_array)
  end
end

puts $solutions.inject(0, :+)
