# The decimal number, 585 = 1001001001(2) (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)


def n_to_binary number
  bin_array = []
  until number == 0
    if number % 2 == 0
      bin_array << 0
    else 
      bin_array << 1
    end
    number = number / 2
  end
  bin_array.join
end

# puts n_to_binary 257


solutions = []

for i in (1...1000000)
  i = i.to_s
  if i == i.reverse
    b = n_to_binary(i.to_i)
    b = b.to_s
    if b == b.reverse
      solutions << i
    end
  end
end

solutions = solutions.map(&:to_i)
puts solutions.inject(0, :+)


# Ways to make this faster (for very large numbers):
# 1. Create an algorithm to find all palindromes in base 10 and then check them in base 2 (would this really be faster? You'd only have roughly 1000 numbers to check)

# Euler demonstrates a cool palindrome generator for base 2, could be fun to come back and build that

# Also, 123.to_s(2) returns 123 in binary, so that's cool




