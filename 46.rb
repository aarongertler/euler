# It was proposed by Christian Goldbach that every odd composite number 
# can be written as the sum of a prime and twice a square.

# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?


# How will we know a number can't be written out this way?
# Answer: We take the number, divide it by two, take the square root of that, and round it down.
# This gives us the biggest square that could feasibly work. We test that square and all smaller squares.
# For each square, subtract it from the original number and see if the result is prime. 
# If you get all the way down to 1^2 and nothing's worked, we have our disproof!

require 'prime'

flag = false
count = 1

until flag == true
  count += 2
  if Prime.prime?(count) then  # Don't analyze prime numbers
    next
  end
  unrounded_root = Math.sqrt(count / 2)
  biggest_root = (unrounded_root - (unrounded_root % 1)).to_i # Find the largest possible "root" of a square that might fit our number
  until biggest_root < 1
    if Prime.prime?(count - 2 * (biggest_root ** 2)) then
      break
    end
    biggest_root -= 1
  end
  if biggest_root == 0
    flag = true
    puts "Success! #{count} disproves the conjecture."
  end
end
