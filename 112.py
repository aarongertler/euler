# Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

# Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

# We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

# Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. 
# In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

# Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

# Find the least number for which the proportion of bouncy numbers is exactly 99%.


# def is_bouncy(n): # This was the wrong approach, too hard to check against the same digit repeating multiple times in a row
# 	s = [int(d) for d in str(n)]
# 	i = 1
# 	while i < len(s) - 1:
# 		print("i:", i)
# 		print("s[i]:", s[i])
# 		print(s[:i])		
# 		print(s[i + 1:])
# 		if (s[i] > max(s[:i]) and s[i] > max(s[i + 1:])) or (s[i] < min(s[:i]) and s[i] < min(s[i + 1:])):
# 			return True
# 		i += 1
# 	return False

def is_bouncy(n):
	status = None
	s = str(n)
	i = 1
	while (status != "bouncy") and i < len(s):
		if (s[i] > s[i - 1]) and status == None:
			status = "increasing"
		if (s[i] < s[i - 1]) and status == None:
			status = "decreasing"
		if (s[i] > s[i - 1]) and status == "decreasing":
			status = "bouncy"
		if (s[i] < s[i - 1]) and status == "increasing":
			status = "bouncy"
		i += 1
	return status == "bouncy"

# print(is_bouncy(525))
# print(is_bouncy(66420))
# print(is_bouncy(155349))

bouncy = 0
n = 99
goal = 0.99 # The proportion we want to reach
flag = False

while flag == False:
	n += 1
	if is_bouncy(n):
		bouncy += 1
	if float(bouncy / n) == goal:
		flag = True

print("Proportion:", float(bouncy / n))
print("Number:", n)


# Solution takes about 5 seconds, Dreamshire's algorithm isn't appreciably faster 
# (does have one less check, though, since it just sets "increasing" and "decreasing" 
# separately and calls "bouncy" if both return true)