# By using each of the digits from the set, {1, 2, 3, 4}, exactly once, 
# and making use of the four arithmetic operations (+, −, *, /) and 
# brackets/parentheses, it is possible to form different positive integer targets.

# For example,

# 8 = (4 * (1 + 3)) / 2
# 14 = 4 * (3 + 1 / 2)
# 19 = 4 * (2 + 3) − 1
# 36 = 3 * 4 * (2 + 1)

# Note that concatenations of the digits, like 12 + 34, are not allowed.

# Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different 
# target numbers of which 36 is the maximum, and each of the numbers 1 to 28 
# can be obtained before encountering the first non-expressible number.

# Find the set of four distinct digits, a < b < c < d, for which the longest 
# set of consecutive positive integers, 1 to n, can be obtained, giving your 
# answer as a string: abcd.


# This is a small enough scope that brute force ought to work -- I think?

# We're allowed to use three total operations. Accounting for placement of parens, our options are:

# a, b, c, d -> parens placement only matters when multiplying and dividing are involved.
# *, *, / :
# (a*b*c) / d = (a*b) * (c / d) = ((a*b)*c) / d... two * in a row make parens irrelevant
# /, *, * :
# (a/b) * c * d, (a/(b*c) * d), a/(b*c*d) are all separate
# /, /, * : ... never mind, see the end of this section.
# From here, we only need to worry about *, /, * and /, *, /
# Using 6, 4, 3, 2 as an example for *, /, *: 
# (a*b) / (c*d), ((a*b) / c) * d are unique (4, 16)
# a * (b/c) * d is not (6*(4/3)*2), a * (b/(c*d)) is not (6*(4/6))
# a * b / c * d is not (8 * 2)
# Using 6, 4, 3, 2 as an example for /, *, /: 
# (a/b) * (c/d), ((a/b) * c) / d are the same (9/4)
# (a / (b*c)) / d is unique (1/4)
# a / (b*(c/d)) is unique (1)
# a / b * c / d is not (9/4)

# ...and I've realized that trying to count up all the nonsense for throwing in addition and subtraction is more than I have patience for.
# I'll let my computer think for a couple of extra seconds instead.

# Looks like there are four combinations for parens placement we'll need -- we can always adjust this later.

from operator import add, sub, mul, truediv
import itertools

digits = list(itertools.combinations(range(1,10), 4))
operations = list(itertools.product([add, sub, mul, truediv], repeat = 3))

# Parens combinations to hit (some are surely redundant, but...:
# (a, b), c, d = REDUNDANT with (a, b), (c, d)
# a, (b, c), d
# a, b, (c, d) = REDUNDANT with (a, b), (c, d)
# (a, b, c), d
# a, (b, c, d)
# (a, b), (c, d)
# ((a, b), c), d
# (a, (b, c)), d
# a, ((b, c), d)
# a, (b, (c, d))

for i in digits:
	for op in operations:
		a, b, c, d = i[0], i[1], i[2], i[3]
		results = []
		else:
			results.append(op[2]((op[0](a, op[1](b, c))), d)) # a, (b, c), d
			results.append(op[1](op[0](a, b), op[2](c, d))) # (a, b), (c, d)

# ...and so on. This is a little too tedious for my tastes, perhaps I'll come back later when I feel fresher.
