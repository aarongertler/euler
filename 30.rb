# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


# Highest number we need to look at: 9^5 * N, where N is the number of digits in that number
# Highest allowable number of digits: Six, as 354294 = 9^5 * 6
# Other rules we'll need to follow: Sum of the N digits must be even (if N is even) or odd (if N is odd) (but does that actually speed us up?)
# We can save time on multiples of 10 by checking whether the sum of N's fifth-power digits = N*10 (since the digits of N*10 will have the same sum, zeroes don't matter)
# Though if that's the case, what about multiples of 100? Hm...


def digitSum number
  number = number.to_s
  power_array = number.chars.map { |digit| digit.to_i ** 5}
  power_array.inject(0, :+)
end

puts digitSum 16


solution_array = []

for i in (2..354294) # Could start higher than 2, keeping it simple for now
  sum_of_digits = digitSum(i)
  if i == sum_of_digits
    solution_array.push(i)
  end
end

puts solution_array.inject(0, :+)   # Takes about 5 seconds to compute (1 on the Dell)

# Ways to make this faster: Skip multiples of 10 as explained above (might make things a bit faster once we account for the extra checks we'd need to build in)
	# Or perhaps get rid of "digitSum" and just do the mapping within the loop