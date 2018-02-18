# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.


# There are 9! unique arrangements of the numbers 1 through 9 =/= 362000, which is manageable
# There are only four ways you can divide up any arrangement by digits (a * b = c): 1, 4, 4; 2, 3, 4; 3, 2, 4; 4, 1, 4
# We don't actually need to test the last two ways, since they'll inevitably mirror other products we've taken already;
# For example, 39 x 186 = 7254 will eventually be mirrored as 186 x 39 = 7254

# So the most basic brute-force procedure = take each permutation, divide it by 1_1_4 and 2_3_4, and grab any matching products
# We can also ignore any permutations that start with a first digit of 1 (1 * a = a, and a can't = a)


# Ruby has an existing permutation method, but here's a recursive algorithm to show the inner workings
# (Courtesy of http://stackoverflow.com/posts/25224355/revisions)

# Basic idea: Take each character in a string and add it to the front of all permutations of the other characters.
# How to get all permutations of the other characters? Same as the above. Recursion!
# So permutation('abc') becomes a + permutation(bc) + b + permutation (ac)...
# And permutation(bc) just returns b + c (bc) and c + b (cb)


# From StackOverflow: https://stackoverflow.com/questions/25224321/find-all-the-possible-permutations-using-ruby-and-recursion

def permutation(string)
  return [''] if string.empty?

  (0...string.size).flat_map { |i|    # flat_map = "return all of our results in one array" (all the permutations)
    chr, rest = string[i], string[0...i] + string[i+1..-1]    # chr = letter we start with
    # print "chr =" + chr
    # print "rest =" + rest
    permutation(rest).map { |sub|  # This is a loop, essentially, where we grab one character at a time, then have the next character be a random selection from our remaining characters (until all the characters are gone)
    chr + sub # All the addition happens at the end, once the recursion chain comes together
    }
  }
end

# puts permutation('1234')

all_permutations = permutation('123456789') # Takes about five seconds to put together
# puts all_permutations.length

all_solutions = []

for i in (0...all_permutations.length)
  perm = all_permutations[i]
  a = perm[0].to_i
  b = perm[1..4].to_i
  c = perm[5..8].to_i
  if a * b == c
    all_solutions.push(c)
    puts c
  end
end  # Takes about 10 seconds to find all solutions, so should take about 15 seconds for the whole thing once we add 2_3_4

for i in (0...all_permutations.length)
  perm = all_permutations[i]
  a = perm[0..1].to_i
  b = perm[2..4].to_i
  c = perm[5..8].to_i
  if a * b == c
    all_solutions.push(c)
    puts c
  end
end

all_solutions = all_solutions.uniq # Remove duplicate products (there were two of them! Huh!)
sum = all_solutions.inject(0, :+)
puts sum
