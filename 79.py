# A common security method used for online banking is to ask the user for three random characters from a passcode. 
# For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

# The text file, keylog.txt, contains fifty successful login attempts.

# Given that the three characters are always asked for in order, analyse the file 
# so as to determine the shortest possible secret passcode of unknown length.


# The math: Every time a digit appears before *and* after another digit, we add another digit to the passcode
# For example, let's look at the first few logs:
# 319, 680, 180, 690, 129, 620, 762
# We know that 3 comes before 1, 1 comes before 9,
# 6 before 8, 8 before 0, 1 before 8, 6 before 9, 9 before 0,
# 1 before 2, 2 before 9, 6 before 2, 2 before 0, 7 before 6...

# And we haven't hit any before/after pairs yet. But let's say we hit 901 somewhere.
# In that case, we know that there's a 1 and a 0 after 9, so we add 2 to the minimum length

# There may be some efficient mathematical way to do it, but I'll start simply:
# Creating a dictionary that logs the "after" numbers for each digit
# This way, we can check whether (for example) 2 is after 7 and 7 is after 2, or whether each digit has a clear hierarchy

from collections import defaultdict # Lets us assign values to keys that don't exist in the dictionary yet
after_log = defaultdict(set) # Don't store one number multiple times

with open("p079_keylog.txt") as f:
	logins = f.read()
f.closed

logins = logins.split('\n')
del logins[-1] # Take out trailing space

# print(logins)

for login in logins:
	first, second, third = login[0], login[1], login[2]
	after_log[first].add(second)
	after_log[first].add(third)
	after_log[second].add(third)

	# if not after_log[first]:
	# 	after_log[first] = [second]
	# else:
	# 	after_log[first].append(second)
	# 	after_log[first] = after_log[first].append(third)

	# after_log[second] = after_log[second] + third

print(after_log) # You can just look at the log of which numbers come after which other numbers and figure out the code in a minute or so, no code needed

# passcode: 73162890

# This turned out to be much simpler than I'd thought, since each digit was only used once.


