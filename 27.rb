# Euler discovered the remarkable quadratic formula:

# n^2+n+41

# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. 
# However, when n=40,40^2+40+41=40(40+1)+41n=40,40^2+40+41=40(40+1)+41 is divisible by 41, 
# and certainly when n=41,41^2+41+41n=41,41^2+41+41 is clearly divisible by 41.

# The incredible formula n^2−79n+1601 was discovered, which produces 80 primes 
# for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

# Considering quadratics of the form:

# n^2+an+bn^2+an+b, where |a|<1000 and |b|≤1000

# where |n| is the modulus/absolute value of n
# e.g. |11|=11 and |−4|=4
# Find the product of the coefficients, a and b, for the quadratic expression that produces 
# the maximum number of primes for consecutive values of n, starting with n=0.

require 'prime'

def newQuadratic(a,b)
  Proc.new { |n| n ** 2 + a * n + b }  # Create a polynomial where we can plug in our values of n
end

# puts newQuadratic(40,41).call(5)

# I'll try brute force first and see what happens. Still getting a sense for the speed of Ruby.

highest_number_of_primes = 0
best_a = 0
best_b = 0

for a in (-999..999).step(2) do  # Both values must be odd, or some values of n will produce even numbers (which aren't prime)
  for b in (-999..999).step(2) do
    n = 0
    quadratic = newQuadratic(a,b)
    until !Prime.prime?(quadratic.call(n))
      n += 1
    end
    if n > highest_number_of_primes
      highest_number_of_primes = n
      best_a = a
      best_b = b
    end
  end
end

puts highest_number_of_primes
puts best_a
puts best_b
puts best_a * best_b

# For the specified range, this takes 15-20 seconds to solve.
# Ways to speed this up: 
# a can't be even and b can't be even, or even values of n will return even numbers (added these checks)

# Yes, that made it much faster!