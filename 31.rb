# In England the currency is made up of pound, £, and pence, p, 
# and there are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:

# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?


# 1 * 2 * 4 * 10 * 20 * 40 * 100 * 200 = 1.28 billion total solutions (shouldn't try to brute-force)

$solution_array = []

# def multiply_and_add_arrays(a,b)
#   c = a.zip(b).map{|x, y| x * y}
#   c.inject(0, :+)
# end

test_coin_array = [10,5,1]
test_goal = 30
solution = []

# def coinLoop array, position, goal, total, solution
#   coin = array[position]
#   if coin == nil
#     return $solution_array
#   end
#   coin_number = 0
#   while total < goal
#     total += coin
#     coin_number += 1
#   end
#   if total == goal
#     solution[position] = coin_number
#     $solution_array.push(solution)
#   end
#   coin_number -= 1
#   solution[position] = coin_number
#   position += 1
#   coinLoop(array,position,goal,total,solution)
# end

# puts coinLoop(test_coin_array,0,test_goal,0,[])


# solution_count = 0

# def coinLoop(array,goal,position,total)
#   coin = array[position]
#   amount_left = goal - total / coin
#   num_coins = coin * amount_left
#   for j in (amount_left..0) # Start with only the largest value
#     total = coin*j
#     if total == goal
#       solution_count += 1
#       total -= coin
#       coinLoop(array,goal,position+1,total)
#     end
#   end
#   solution_count
# end


# Trying a recursive array-style solution. 
# Basic idea: # An array of 201 zeroes (at first). array[i] = the number of ways to make change for i pence. 
# As long as we're making change for an amount (n) below our second-lowest coin (5), we'll only have 1 way to make change
# (by using n 1-pence coins). But once we reach n = 5, we suddenly have two options: a 5-pence coin or 5 1-pence coins.
# This continues until we reach n = 10. At that point, we have four options: a 10-pence coin, 2 5-pence coins, 
# 1 five and 5 ones, or 10 ones. When we hit 20, we have 4*4 options (since we can make two tens in four different ways each)
# plus one more option (just using a 20). 

# So, for any value given a set of coins, the number of possible combinations = the number of ways you can break down the biggest
# denominator of coin * the number of coins of that type you can fit into the value (but order doesn't matter)
# So 6 could be 1+1+1+1+1+1, 2+1+1+1+1, 2+2+1+1, or 2+2+2 = 4 ways (what's the permutation logic to use here? Not sure...)


# test_goal = 30
goal = 200
# test_array = [1,5,10]
coin_array = [1,2,5,10,20,50,100,200] # Stores the values of all our coins
ways = Array.new(goal+1){ |i| 0 }
ways[0] = 1

# puts ways.length

for i in (0..coin_array.length - 1)      # Look at each coin in the array (each time we loop through the coins, we'll update our "ways" array to see how many ways we can make each number with the coins we've seen so far)
  for j in (coin_array[i]..goal)    # For all values between the coin's value and our goal value, see how many permutations this coin adds
    ways[j] += ways[j - coin_array[i]]   # For value j, add a number of new ways to make it equal to the ways we can make j - (coin value) 
    	# Why do we subtract the value of the coin we're looking at to find our array index? Because we're pretending to add exactly that coin to the number we're looking at.
    	# Using 2-pence coins in addition to 1-pence coins, how many ways can we make 8? Well, we know we can add our new coin, and then we need 6 more pence, so let's see how many ways there are to make 6!
    	# When we add 5-pence coins, we have 7 ways to make 8, not 5 -- because we can use a 5-pence coin, and then add 3 in (let's check) two different ways!
  end
end
 
puts ways[200]

# Super fast! Hooray for dynamic programming!
[0 1 2 3 4 5 6 7 8 9 10 11]
[1 1 1 1 1 1 1 1 1 1 1 1]
[1 1 2 2 3 3 4 4 5 5 6 6]
[1 1 2 2 3 4 5 6 7 8 10 11]
 # Check out how many ways there are to make 10 when 5s are available -- 6 ways that use only 1 and 2, or we could add a 5 and have (let's check) 4 ways to add 5 to our original 5-pence coin
 # (5 + 5, 5 + 2 + 2 + 1, 5+2+1+1+1, 5+1+1+1+1+1)


# For an example of the last note: When we look at the 20p coin for the value 25p, we take the number of ways we can make 5p and add them
# to the number of ways we can make "25", since we can now add the 20p coin to any of those 5p combinations as a new way of making 25
# In the end, we wind up adding: "Okay, so we were acting as though we only had coins up to 50p. When we add 100p coins, we now get to make any 
# number (n) greater than 100 by looking at our past ways to make (n-100) and adding a 100p coin to them. Those are the only new combinations
# we get by having access to the 100p coin, because (clearly) no combination below 100p would be affected."




# int target = 200;
# int[] coinSizes = { 1, 2, 5, 10, 20, 50, 100, 200 };
# int[] ways = new int[target+1];
# ways[0] = 1;
 
# for (int i = 0; i < coinSizes.Length; i++) {
#     for (int j = coinSizes[i]; j <= target; j++) {
#         ways[j] += ways[j - coinSizes[i]];
#     }
# }
