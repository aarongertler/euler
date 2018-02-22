# A googol (10^100) is a massive number: one followed by one-hundred zeros; 
# 100^100 is almost unimaginably large: one followed by two-hundred zeros. 
# Despite their size, the sum of the digits in each number is only 1.

# Considering natural numbers of the form, a^b, where a < 100 and b < 100, what is the maximum digital sum?


# If a is a multiple of 10, get rid of it, the digit sum will always be 1

def digit_sum n
	n.to_s.chars.map(&:to_i).reduce(:+) # "chars" splits up the digits so we can reduce them
end

highest = 0

for a in 2..100
	if a % 10 == 0 then next
	end
	for b in 2..100
		highest = [highest, digit_sum(a ** b)].max
	end
end

puts highest

# Constraints we could add: Check the number of digits and get rid of the number if the sum wouldn't be high enough even for all digits = 9
# 	Or just do a bit of math and set better constraints for a and b (50 is reasonable, given the number of digits we can produce)
