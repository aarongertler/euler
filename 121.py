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
# Five turns, P(win) = P(5 blue) + P(four blue) + P(three blue)

