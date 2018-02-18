require 'prime'
require 'benchmark'

# Consider all integer combinations of a^b for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

# 2^2=4, 2^3=8, 2^4=16, 2^5=32
# 3^2=9, 3^3=27, 3^4=81, 3^5=243
# 4^2=16, 4^3=64, 4^4=256, 4^5=1024
# 5^2=25, 5^3=125, 5^4=625, 5^5=3125
# If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:

# 4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

# How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?


# This one looks really straightforward (assuming that 100^100 doesn't just murder Ruby) (but testing seems to show that it does not)

allTerms = []

# for i in (2..100)
#   for j in (2..100)
#     allTerms[i ** j] = 1   # If huge index values are a problem, just check if the value exists in the array yet and push if not
#     if i != j
#       allTerms[j ** i] = 1
#     end
#   end
# end

# We did hit a memory error with the above, so I assume the huge index values were a problem. Let's try again:

primetime = Benchmark.measure {
	for i in (2..100)
	  for j in (2..100)
	    i_j = i ** j
	    if Prime.prime?(i)
	    	allTerms.push i_j
	    elsif !allTerms.include?(i_j)
	      allTerms.push i_j
	    end
	  end
	end
}

nonprime = Benchmark.measure {
	for i in (2..100)
	  for j in (2..100)
	    i_j = i ** j
	    if !allTerms.include?(i_j)
	      allTerms.push i_j
	    end
	  end
	end
}

puts primetime # this is about 20% faster
puts nonprime


# puts allTerms.length # Works after 4 seconds in Ruby (with the new Dell Inspiron)

# Ways to make this faster:
# Any exponential where the base is prime will definitely be unique, push it automatically
