# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576

# By concatenating each product we get the 1 to 9 pandigital, 192384576. 
# We will call 192384576 the concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, 
# giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
# concatenated product of an integer with (1,2, ... , n) where n > 1?


# We know the largest number will start with 9
# We know the integer will be 2, 3, or 4 digits (unless 9 really is the biggest)
# We know the first digit of the integer will be 9
# We know the integer will not contain zero
# Let's start with these factors and try this out

pandigitals = []

def is_pandigital number
  n = 1
  new_number = number
  while new_number.to_s.length < 9
    n += 1
    new_number = [new_number,number*n].join.to_i
  end
  if new_number.to_s.chars.sort.join == '123456789'
    new_number
  else
    0
  end
end

for i in (91..99)
    pandigitals << is_pandigital(i)
end

for i in (911..999)
    pandigitals << is_pandigital(i)
end

for i in (9111..9999)
    pandigitals << is_pandigital(i)
end

puts "Largest number: #{pandigitals.max}"

# Ways to make this faster: You could do more filtering up front to narrow the range of numbers you look at, but this is quite fast already