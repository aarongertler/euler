# Consider the fraction, n/d, where n and d are positive integers. 
# If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

# If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

# It can be seen that 2/5 is the fraction immediately to the left of 3/7.

# By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, 
# find the numerator of the fraction immediately to the left of 3/7.


# Let's try to find a shortcut right away. What's a number that is very, very close to 3/7s, but slightly smaller?
# For example, take 3x/7x, where 7x is the largest multiple of 7 under 1,000,000. 
# If we find that (3x - 1) is relatively prime with 7x, that should work. If not, we try again with 3(x-1) and 7(x-1).

# This might not work -- maybe there's some random fraction that fits between 3x/7x and (3x - 1)/7x -- but it seems pretty likely to work

from sympy import gcd

x = 1000000 // 7
three_test = 3 * x
seven_test = 7 * x

while gcd((three_test - 1), seven_test) != 1:
	three_test -= 3
	seven_test -- 7

print(three_test - 1)

# Yep, that was easy. Might be my fastest solution ever?

# Other solutions I've seen just start with 3/7
# And then find the value of n closest to 1000000 such that
# int((3/7)*n) / n is smaller than 3/7 (at least, that's my interpretation)

