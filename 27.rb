# Euler discovered the remarkable quadratic formula:

# n^2+n+41

# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤390≤n≤39. 
# However, when n=40,40^2+40+41=40(40+1)+41n=40,40^2+40+41=40(40+1)+41 is divisible by 41, 
# and certainly when n=41,41^2+41+41n=41,41^2+41+41 is clearly divisible by 41.

# The incredible formula n^2−79n+1601 was discovered, which produces 80 primes 
# for the consecutive values 0≤n≤790≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

# Considering quadratics of the form:

# n^2+an+bn^2+an+b, where |a|<1000|a|<1000 and |b|≤1000|b|≤1000

# where |n||n| is the modulus/absolute value of n
# e.g. |11|=11| and |−4|=4
# Find the product of the coefficients, a and b, for the quadratic expression that produces 
# the maximum number of primes for consecutive values of n, starting with n=0.

require 'prime'

def newQuadratic(a,b)
  Proc.new { |n| n ** 2 + a * n + b }
end

# puts newQuadratic(40,41).call(5)

# I'll try brute force first and see what happens. Still getting a sense for the speed of Ruby.

highest_number_of_primes = 0
best_a = 0
best_b = 0

for i in (-1000..1000)
  for j in (-1000..1000)
    n = 0
    quadratic = newQuadratic(i,j)
    until !Prime.prime?(quadratic.call(n))
      n += 1
    end
    if n > highest_number_of_primes
      highest_number_of_primes = n
      best_a = i
      best_b = j
    end
  end
end

puts highest_number_of_primes
puts best_a
puts best_b

# For the specified range, this takes 15-20 seconds to solve.
# Ways to speed this up: 
# Clearly, a and b can't both be even, or even values of n will return even numbers
# Also, a can't be odd while b is even, or (again) any even value of n will return an even number
# Thus, b can't be even. It seems like a can still be even, but I'd want to look into that further...
