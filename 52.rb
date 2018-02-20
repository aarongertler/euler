# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.


# Well, this is a nice break after 51. Sheesh.
# I feel like x would have to be a multiple of 9, since those are traditionally the numbers that can be reversed through integer multiplication
# (as in the given example). I'll try that first, even if I can't prove the idea
# Also, the first digit of x has to be 1 and the second digit can't be above 6, or 6x will have too many digits
	# (though I'll only include this if the code is kind of slow -- my guess is that it will move very quickly)

flag = false
i = 100008 # Answer must be six digits (since we need six different starting digits for our six results)

def digits n
	n.to_s.chars.sort.join
end

def all_equal?(*elements) # From https://stackoverflow.com/questions/12846080/three-way-comparison-in-ruby
  elements.all? { |x| x == elements.first }
end

while flag != true
	if all_equal?(digits(i), digits(2*i), digits(3*i), digits(4*i), digits(5*i), digits(6*i))
		flag = true
		puts "The answer is #{i}"
	end
	i += 9 # Answer works with this, so might as well speed things up by a factor of 9
end