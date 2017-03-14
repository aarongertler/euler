# A unit fraction contains 1 in the numerator. 
# The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2 =   0.5
# 1/3 =   0.(3)
# 1/4 =   0.25
# 1/5 =   0.2
# 1/6 =   0.1(6)
# 1/7 =   0.(142857)
# 1/8 =   0.125
# 1/9 =   0.(1)
# 1/10  =   0.1

# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. 
# It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.


# Mathematically, this seems impossible to "prove" in a reasonable way.
# After all, how can we tell whether a recurring cycle is really hundreds of digits long?
# For now, we'll look at the cycles we can get by dividing Ruby floats and see if that works out.

require 'prime'

def getFraction(n)
  n = n.to_f
  return (1/n).to_s[2..-1] # cuts out 0. from our string

end

# puts getFraction(8)
# puts getFraction(13) # 16 digits, enough for two repetitions of 6 digits

# Hm. If 7 and 13 both have 6-digit cycles, what are the odds that we won't get a longer cycle before we hit 1000?
# So how can we find a longer cycle?
# I suppose we could start by identifying all numbers with 16 digits and no recurring patterns...
# Let's try a few filters to get an answer. That can at least help us narrow down, and maybe see patterns.

# Also, we start rounding in weird ways beyond the 15th number, so cycles of length 15 or more are the first thing to filter.

# Another note: If n has a recurring cycle of length z, a*n also has a cycle of length z
# In other words, we only need to check prime numbers

# $longest_number = 0 # Stores the number that has given us our longest cycle so far
# $longest_cycle = 0 # Stores the length of our longest cycle so far

# test_array = (1..1000).to_a

# prime_filter = lambda { |n| Prime.prime?(n) }
# cycle_filter = lambda { |n| getFraction(n).length > 15 }

# long_array = test_array.select(&prime_filter)

# print long_array

# test_array.each do |n|
#   puts n.to_s + ": " + getFraction(n)
# end

# Just looking over some early results, I see that 93 (for example) doesn't recur within 16 digits.
# Thus, there are probably many candidates that don't recur within 16 digits.

# Looks like we'll need to look at longer fractions. How can we calculate fractions "by hand"?
# Remainders, maybe? Remainder of 1/7 = 1, the first digit of the fraction 1/7. Remainder of 1*10 / 7 = 10/7 = 3.
# 3*10 / 7 has a remainder of 2. 2*10 / 7 has a remainder of 6. 60/7, 4. 40/7, 5. 50/7, 1. We've already seen that digit,
# so now it looks like we're looping. (For 8, 1/8 -> 1 -> 10/8 -> 2 -> 20 / 8 -> 4 -> 40/8 -> 0, so the fraction stops
# after three digits.)

# (Why do this remainder stuff? Well, 1/7 has a 0 in the ones place, since no sevens go into one. But in the tenths place,
# it has a 1, because one 0.7 goes into 1. That leaves 0.3 "left" for the hundredths place, and four 0.07s go into 0.3. 
# And so on. Once we get the same remainder at some point, the pattern has to repeat itself, and we have a cycle.)

def remainderCycle(n) # Find how long the cycle is for a particular number
  cycle_length = 1
  remainder = 1
  found_remainders = []
  until found_remainders[remainder] != nil
    found_remainders[remainder] = cycle_length
    remainder = (remainder*10) % n
    cycle_length += 1
  end
  cycle_length - found_remainders[remainder]
end

# puts remainderCycle(93)

longest_length = 0
longest_number = 0

for i in 7..1000
  this_length = remainderCycle(i)
  puts this_length
  if longest_length < this_length
    longest_length = this_length 
    longest_number = i
  end
end

puts longest_length
puts longest_number
