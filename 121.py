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
# Three turns, P(win) = (1/2 * 1/3 * 1/4) + (1/2 * 1/3 * 1/4) RBB + (1/2 * 2/3 * 1/4) BRB + (1/2 * 1/3 * 3/4) BBR = 1 + 1 + 2 + 3 / 24 = 8/24 = 1/3
# Four turns, P(win) = 1 + 1 + 2 + 3 + 4 / 5! = 11/120
# Five turns, P(win) = P(five blue) + P(four blue) + P(three blue)
# = 1 + (1+2+3+4+5) + (5 choose 2 = 10 arrangements of probabilities, which sum to...)

# ...so what's the shorthand for what this sums to?
# The denominator of our final fraction will always be (n+1)!, where n is the number of turns played.

# The number of terms we add to find the numerator = 1 + n choose 1 + n choose 2... + n choose 7 (in the case of n = 15)
# For each term, we multiply together all of the numerators of the "turns" where we find red discs
# So if we pick 7 blue / 7 red, we have 15 choose 7 ways for that to happen, meaning 15 choose 7 "combinations" of numerators,
# no repeats, between 1 and 15.

# We can grab all of these by finding all permutations of 1-15, grabbing and sorting the first 7 terms of each, then keeping the unique "sets" of numbers
# The same procedure applies to finding all the other terms for each probability.
# Is there a shorter way to find the unique combinations of x terms, without having to find all the permutations of all 15 terms first?
# Maybe, but since we only have to find ALL the permutations one time (for each number from 2-15), trying brute force first seems... fine?

def permutations(list): # Return all permutations of a list of numbers, in list form




# Remember to do lots of mapping here!

# Commit for EA forum
# Commit #2 for EA forum