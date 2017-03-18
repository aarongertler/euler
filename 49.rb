# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, 
# is unusual in two ways: (i) each of the three terms are prime, 
# and (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
# exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?

require 'prime'

i = 1001

until i > 9876 # End loop at the last number which could feasibly begin a permutation addition sequence (the third-largest 9876 permutation)
  if Prime.prime?(i)
    i_perm = i.to_s.chars.sort.join
    biggest_increase = (10000 - i) / 2
    j = [(i_perm[2].to_i - i_perm[1].to_i * 40),2].max # Imagine n = 1234. The second-smallest permutation is 1243. The third-smallest is 1324. The difference between the smallest and largest of these is 81. j * 2 must > 81. Thus, j > 40. Specifically, j > 40 * (third-smallest digit - second-smallest digit). j can be bounded more rigorously, I think, but the loop runs fast enough that I'll pass for now.
    until j > biggest_increase
      second = i + j
      if i_perm == second.to_s.chars.sort.join && Prime.prime?(second)
        third = second + j
        if i_perm == third.to_s.chars.sort.join && Prime.prime?(third)
          puts "Success! The numbers are #{i}, #{second}, and #{third}."
        end
      end
      j += 2 # j must be even (because, added to an odd number, it must return an odd number)
    end
  end
  i += 2 # i must be odd (because it is prime)
end

# Ways to make this faster:
# 1. Doing more math to put harder restrictions on i-values and j-values worth checking (especially if we want to check numbers with more digits)
# 2. For this particular code, going for readability (starting j at 2, for example) may be better than going for more speed.