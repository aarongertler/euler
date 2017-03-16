# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they are not included.


# Solutions could be as high as 9! * 7 (a seven-digit number), because 9! * 8 is still a seven-digit number

$fact_array = [] # Array to store factorial values

for i in (0..9)
  $fact_array[i] = (1..i).inject(:*) || 1
end

def factorialSum number
  sum = 0
  str = number.to_s
  for i in (0...str.length)
    digit = str[i].to_i
    # sum += (1..digit).inject(:*) || 1 # 0! = 1
    sum += $fact_array[digit] # Decided to speed things up a bit by caching factorial values, since there are only 10 of them
  end
  sum
end

# puts factorialSum 145

highest_possible = factorialSum 9999999

solutions = []

for i in (3..1000000)
  if factorialSum(i) == i
    solutions.push(i)
  end
end

puts solutions
solution_sum = solutions.inject(0, :+)
puts solution_sum


# Other filtering rules: Any odd number not containing a 1 (factorial sums can't be odd unless 1 is involved)
# But checking for oddness and non-one-containing-ness might be slower than just checking the number, would need to test that