# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, 
# is unusual in two ways: (i) each of the three terms are prime, 
# and (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
# exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?

require 'prime'

i = 1001

until i > 9786 # End loop at the last number which could feasibly begin a permutation addition sequence (the third-largest 9876 permutation)
  if Prime.prime?(i)
    i_perm = i.to_s.chars.sort.join
    biggest_increase = (10000 - i) / 2 # The largest amount we can increase by and still have a four-digit number
    increase = 54 # No number exists where the smallest and third-smallest permutations are less than 90 apart (e.g. 1234 and 1324), and the difference must be a multiple of 18 (multiples of 9 "rotate" numbers, and the difference must be even to leave only odd numbers)
    until increase > biggest_increase
      second = i + increase
      if i_perm == second.to_s.chars.sort.join && Prime.prime?(second)
        third = second + increase
        if i_perm == third.to_s.chars.sort.join && Prime.prime?(third)
          puts "Success! The numbers are #{i}, #{second}, and #{third}."
        end
      end
      increase += 18 # As noted in line 18, the difference must be a multiple of 18
    end
  end
  i += 2 # i must be odd (because it is prime)
end

# Ways to make this faster (though it already runs in half a second):
# Doing more math to put harder restrictions on i-values and j-values worth checking (especially if we want to check numbers with more digits)
#   For example, we could turn each number into an array of permutations, only keep numbers with at least three prime permutations, and then test differences
#     between those permutations
#   Or you could just test the addition of 3330 to your starting numbers (as this creates another permutation)
#     This doesn't capture all relevant numbers for all digit counts, but it's a great shortcut to test many possibilities
#     And there are other similar "rotation" numbers we could check specially (e.g. 4500)