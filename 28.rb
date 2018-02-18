# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

# Hm. Mathematically, this is pretty easy to just reason out.
# An N x N spiral will have (N - 1)/2 "layers" of diagonal numbers (e.g. two layers in a 5 x 5 spiral)
# The sum for one "layer" is 1 + (1+2) + (1+4) + (1+6) + (1+8) = 1 + 4 + 20 = 1 + 4(6)
# The sum for two "layers" is the sum for (sum(1 layer)) + (1+12) + (1+16) + (1+20) + (1+24) = 1 + 4 + 20 + 4 + 72 = 1 + 4(25)
# Which is the same as 1 + (1+2) + (1+2+2) + (1+2+2+2) + (1+2+2+2+2) + (1+2+2+2+2+4) + (1+2+2+2+2+4+4)...

# How many twos do we add? 10 for the first layer, 16 for each layer after. 
# How many fours do we add? 0 for the first layer, 10 for the second layer, 16 for each layer after.
# How many sixes do we add? 0, then 0, then 10, then 16... etc.
# Sum(Nth layer) = 2*N*10 + 2*(N-1)*16 + 2*(N-2)*16... + 4  (3rd layer = 76 = 2*2*10 + 2*1*16 + 0 + 4)

sum = 1 # Start with the "zero" layer (just 1)

for i in (1..500) # 500 "layers" in a 1001 x 1001 spiral
  sum += 4       # 4*N
  sum += 20*i    # 2*N*10
  for j in (1...i) # for each layer, we add another set of 16s -- if i = 3, we'll add 2*16*(3-1) and 2*16*(3-2) (which is correcet, as you can see above)
    sum += 32*(i-j)    # 2*(N-1)*16
  end
end

puts sum

# There are ways to write this that are shorter, not sure if any are worth giving up on clarity for 
# (one-liners are possible, using the insight that the sum of new corners is 4 * (a square number) - 6*(layer count))
# So for the second layer, sum of corners is 4 * 25 - 4 - 8 - 12 = 4*5^2 - 6 * (5-1) (pattern continues for everything else)