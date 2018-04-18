# Comparing two numbers written in index form like 2^11 and 3^7 is not difficult, 
# as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

# However, confirming that 632382^518061 > 519432^525806 would be much more difficult, 
# as both numbers contain over three million digits.

# Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file 
# containing one thousand lines with a base/exponent pair on each line, determine 
# which line number has the greatest numerical value.


# We're going to need some logarithms!

# log x^y = y * log(x)   Example: log(2^5) = log(32) = 5*log(2)

# If we find the largest log, we'll easily find the largest number. 
# Very simple. This is 10% difficulty for a reason (though splitting the string was annoying)


from math import log


pairs = open('p099_base_exp.txt', 'r').read().split('\n')

# print(pairs)

max_value = 0
max_count = 0

for count, pair in enumerate(pairs, start = 1): # Enumerate lets us easily keep track of the line number without having to increment a "count" variable ourselves
	b, e = pair.split(',')
	value = int(e) * log(int(b))
	if value > max_value:
		max_value = value
		max_count = count

print("Max value at line:", max_count) # Answer is instant

