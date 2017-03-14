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
# The sum for three "layers" is the sum for (sum(2 layers)) + (1+30) + (1+36) + (1+42) + (1+48) = 1 + 4 + 20 + 4 + 72 + 4 + 156 = 1 + 4(65)
# Which is the same as 1 + (1+2) + (1+2+2) + (1+2+2+2) + (1+2+2+2+2) + (1+2+2+2+2+4) + (1+2+2+2+2+4+4)...

# 1*4*(N) + 2*10 + 2*4*4*(N - 1) + 4*10 + 4*16(N-2)...    (The center +1 is stored in the addition of 64^0)
# 4*N + (2N * 10 + 2N(N-1)...) summed over N (until you hit 2^N(N-N))

# On second thought, this recursive pattern is a bit tricky to calculate mentally. Let's try it in code!
# (Building an array of arrays would probably be easier, but...)


# How many twos do we add? 10 for the first layer, 16 for each layer after. 
# How many fours do we add? 0 for the first layer, 10 for the second layer, 16 for each layer after.
# Sum(Nth layer) = 2*N*10 + 2*(N-1)*16 + 2*(N-2)*16... + 4  (3rd layer = 76 = 2*2*10 + 2*1*16 + 0 + 4)

sum = 1 # Start with the "zero" layer (just 1)

for i in (1..500) # 500 "layers" in a 1001 x 1001 spiral
  sum += 4       # 4*N
  sum += 20*i    # 2*N*10
  for j in (1...i)
    sum += 32*(i-j)    # 2*(N-1)*16
  end
end

puts sum