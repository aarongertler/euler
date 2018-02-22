# It is possible to show that the square root of two can be expressed as an infinite continued fraction.

# √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

# By expanding this for the first four iterations, we get:

# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

# The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, 
# is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

# In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?


# Each fraction follows the pattern: the nth fraction = x/y, where x = x(n-1)*2 + x(n-2) and y = y(n-1) + x(n-1)

x = 3
y = 2
x_two_back = 1
x_one_back = 1
more_digits = 0

def digits n 
	Math.log10(n).to_i + 1
end

for i in 2..1000
	y = x + y
	last_x = x
	x = 2*x + x_two_back
	x_two_back = last_x
	if digits(x) > digits(y)
		more_digits += 1
	end
end

puts more_digits # You could also just work this out mathematically, perhaps, with a simple pattern, but this code is quite fast anyway
