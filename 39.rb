# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
# there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximised?


# Finding solutions for right triangles (a,b,c)
# Let's assume a is the longest side

# require 'math'

def find_solutions perimeter
  solutions = []
  for a in (3...perimeter / 3) # Smallest side, will be less than 1/3 of the perimeter
    for b in (a + 1...perimeter / 2)
      c = perimeter - a - b
      next if c > 500 # Can't have a real triangle formed if c > a + b (this doesn't save much time, if any, still mathematically good to remember)
      # puts c if c > 500 # Seems like our "next" is properly skipping over the Pythagorean check, since we never print anything
      if a ** 2 + b ** 2 == c ** 2
        solutions << [a,b,c]
      end
    end
  end
  solutions.length
end

# puts find_solutions 30 # One solution -> 5, 12, 13

answer = 0
highest = 0

for i in (120..1000).step(2) # Only even perimeters can work -- we either have the sum of three even square numbers, or the sum of one even and two odds
  solution_count = find_solutions(i)
  if solution_count > highest
    highest = solution_count
    answer = i
  end
end

puts answer # 3 seconds, not great compared to what we could be getting (though some of that might be Ruby's fault)

# Ways to do this faster: Use properties of Pythagorean triples to get down to well under a second 
# For example, see http://mathworld.wolfram.com/PythagoreanTriple.html
# Or use odd values of x and values of n > x to check a,b,c combinations where:
#   A = 2*x*n - x ** 2
#   B = 2*(n ** 2) - 2*x*n
#   C = 2*(n ** 2) - 2*x*n + x ** 2
# This will always give us Pythagorean triples (x = 1, n = 2 is 3, 4, 5, for example),
# so all we have to do is note which triples appear more often than others
