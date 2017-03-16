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
# 1. Create an algorithm to generate palindromes in base 2 and check them in base 10
# Because any x-digit number (e.g. '123') corresponds to two palindromes of 2x - 1 and 2x digits
# ('12321', '123321'), there are only about 2000 palindromes below 1000000 we'd ever need to check

# Euler demonstrates a cool palindrome generator for base 2, could be fun to come back and build that




