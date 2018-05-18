# Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

# Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

# We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

# Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. 
# In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

# Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

# Find the least number for which the proportion of bouncy numbers is exactly 99%.


def is_bouncy(n):
	s = str(n)
	i = 1
	while i < len(s) - 1:
		if (s[i] >= max(s[:i - 1]) and s[i] >= max(s[i + 1:])) or (s[i] <= min(s[:i - 1]) and s[i] <= min(s[i + 1:])):
			return True
		i += 1
	return False

# print(is_bouncy(525))
# print(is_bouncy(66420))
# print(is_bouncy(155349))

bouncy = 0
n = 99
flag = False

while flag == False:
	n += 1
	if is_bouncy(n):
		bouncy += 1
	else:
		print("Non-bouncy n:", n)
	if float(bouncy / n) == 0.9:
		flag = True

print("Proportion:", float(bouncy / n))
print("Number:", n)

