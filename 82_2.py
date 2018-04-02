# Using this to save and try to understand aspects I liked of various solutions to 82 from others
# But the only one I'll save and upload is Dreamshire's, since that's already public

# matrix = [[int(numb) for numb in line.split(',')] for line in open('p082_matrix.txt', 'r')]

matrix = [[131,673,234,103,18],
         [201,96,342,965,150],
         [630,803,746,422,111],
         [537,699,497,121,956],
         [805,732,524,37,331]]

n, m = len(matrix), len(matrix[0]) 
cost = [matrix[i][-1] for i in range(n)] # Tracks the last column, continues to add potential sums
print(cost)

# General idea for this function: Find the lowest value you can end up with based on the impact of each new column
# From a given number in a given column, shows the value of the lowest sum we can get, starting from that number, based
# on the sums of the future numbers we know we'll encounter

for i in range(m-2, -1, -1): # Starting at next-to-last column and working backwards to index 0
    cost[0] += matrix[0][i] # Add the top row of numbers to the upper-right corner as we go, just to be efficient
    for j in range(1, n): # For each row, find the sum of the last column for that row by...
        # ...first finding the sum derived from adding the number to the left of our spot in the last column
        # The "min function" checks whether it's better to go left or go up and then left from a given column
        cost[j] = min(cost[j], cost[j-1]) + matrix[j][i]
    for j in range(n-2, -1, -1):
        # The "min function" here checks whether it's better to go left or go down and the left from a given column
        # (By this point, cost[j] can be the value of going left, so we make that an option in the min function)
        cost[j] = min(cost[j], cost[j+1] + matrix[j][i])
    print(cost)

# After one round of this in the test matrix, our last column is:
# 121 -> value of top row, simple
# 1086 -> 965 + 121, shows that it's better to (if you end up at 965) go up and right than it is to just go right
# 533 -> 111 + 422, straight line -- from 422, the best place to go is 111
# 489 -> 121 + 37 + 336, shows that it's better to go down and right from 121 than it is to just go right
# 368 -> 37 + 331, straight line

# And so on, for all the other rounds

print("Minimum path in", n, "by", m, "matrix =", min(cost))

matrix = [[131,673,234,103,18],
         [201,96,342,965,150],
         [630,803,746,422,111],
         [537,699,497,121,956],
         [805,732,524,37,331*]]
