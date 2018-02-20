# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.


# Ruby can actually handle 1000 ^ 1000. 
# ...I guess we'll try brute force? 
# Can't wait to see the error message

sum = 0

for i in (1..1000)
  sum += (i ** i)
end

puts sum  # Well, we do get a number. Was it rounded automatically?

# ...no, it was not. Now I see why this problem was so popular.

# Lots of fun assembly-language solutions within Euler as a treat!