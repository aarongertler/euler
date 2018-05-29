# A bag contains one red disc and one blue disc. In a game of chance a player takes a disc at random and its colour is noted. 
# After each turn the disc is returned to the bag, an extra red disc is added, and another disc is taken at random.

# The player pays £1 to play and wins if they have taken more blue discs than red discs at the end of the game.

# If the game is played for four turns, the probability of a player winning is exactly 11/120, 
# and so the maximum prize fund the banker should allocate for winning in this game would be £10 before they would expect to incur a loss. 
# Note that any payout will be a whole number of pounds and also includes the original £1 paid to play the game, so in the example given 
# the player actually wins £9.

# Find the maximum prize fund that should be allocated to a single game in which fifteen turns are played.


# After one turn, P(win) = 1/2
# After two turns, P(win) = 1/2 * 1/3 = 1/6
# Three turns, P(win) = (1/2 * 1/3 * 1/4) + (1/2 * 1/3 * 1/4) RBB + (1/2 * 2/3 * 1/4) BRB + (1/2 * 1/3 * 3/4) BBR = 1 + 1 + 2 + 3 / 24 = 7/24
# Four turns, P(win) = 1 + 1 + 2 + 3 + 4 / 5! = 11/120
# Five turns, P(win) = P(five blue) + P(four blue) + P(three blue)
# = 1 + (1+2+3+4+5) + (5 choose 2 = 10 arrangements of probabilities, which sum to...)

# ...so what's the shorthand for what this sums to?
# The denominator of our final fraction will always be (n+1)!, where n is the number of turns played.

# The number of terms we add to find the numerator = 1 + n choose 1 + n choose 2... + n choose 7 (in the case of n = 15)
# For each term, we multiply together all of the numerators of the "turns" where we find red discs
# So if we pick 7 blues or 7 reds, we have 15 choose 7 ways for that to happen, meaning 15 choose 7 "combinations" of numerators,
# no repeats, between 1 and 15.

# We can grab all of these by finding all permutations of 1-15, grabbing and sorting the first 7 terms of each, then keeping the unique "sets" of numbers
# The same procedure applies to finding all the other terms for each probability.
# Is there a shorter way to find the unique combinations of x terms, without having to find all the permutations of all 15 terms first?

from itertools import combinations, chain # We don't want to double-count "red disk on turns 1 and 5" and "red disk on turns 5 and 1", so we won't be using permutations
from math import factorial
import numpy as np


# print(list(combinations([1, 2, 3, 4], 2)))

# for i in combinations([1, 2, 3, 4], 2):
# 	print(i)


def winning_odds(turns): # Odds of getting mostly blue disks after a certain number of turns
	n_list = list(range(1, turns + 1))
	denom = factorial(turns + 1)
	num = 1 + sum(n_list) # Numerator of the fraction that shows us our odds
	if turns % 2 == 1:
		for i in range(2, int(turns / 2) + 1):
			perms = list(combinations(n_list, i))
			# print("Perms:", perms)
			prods = np.array(list(map(np.prod, perms)), dtype='int64') # Fixed scalar overflow issue by moving to a more permissive numpy dtype: https://stackoverflow.com/questions/7559595/python-runtimewarning-overflow-encountered-in-long-scalars
			# print("Prods:", prods)
			num += sum(chain(prods))
	print("Odds:", num, "/", denom)
	print("Prize fund:", denom // num)

winning_odds(15) # Instantaneous, though Dreamshire's more "pure" method is certainly faster (my solution starts to get sluggish around 20 turns)