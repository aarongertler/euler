# Solving sudoku puzzles

# How will this actually work?

# Based on some outside research on Sudoku algorithms (I think the problem encourages this),
# I find that the main method is depth-first recursion: Add the first working number you can to each sqaure, 
# then back up to the most recent square we haven't disproven if you find that you have an ineligible square
# This creates an elegant algorithm, but also a lot of backtracking (though it's reasonably fast)

# For example, for the puzzle on Euler's website, we'd fill in "4" for the top-left corner, then "5" for the next square,
# but "5" wouldn't work, because we'd eventually find that no other number works for the real "5" in this row.
# So we'd keep backtracking to other mystery numbers, eventually running out of reasonable combinations to try after filling in our bad "5".
# So instead we'll try 7, it will fail in the same way, we'll try 8, it will succeed, we'll move to recur attempts for the next mystery number...

# The other option is to loop over the puzzle again and again, filling in squares with only one option, then using our new fill-ins to keep eliminating 
# possibilities for squares we couldn't figure out before...
# ...but looking at the first puzzle, I'm not sure whether that will fill everything in.

# Still, I'll try my algorithm before I move to something recursive.

import re

puzzle_rows = open('p096_sudoku.txt', 'r').read().split('\n')

puzzles = ["".join(puzzle_rows[x+1:x+10]) for x in range(0, len(puzzle_rows), 10)]

# print(puzzles) 

def same_row(a, b): return (a // 9 == b // 9)
def same_column(a, b): return (a - b) % 9 == 0 # indices subtract to create a multiple of 9: 6 and 24 are in the same column, for example
def same_block(a, b): return (a // 27 == b // 27 and (a % 9) // 3 == (b % 9) // 3) # Biggest separation within a square is 26 "places"; 10-11-12 are 1-2-3 more than a multiple of 9, as are 1-23 and 19-20-21 (all indices in the same block)

def solve(puzzle):
	while '0' in puzzle: # There are still unsolved squares
		replaced = False
		# print(puzzle)
		squares = [a.start() for a in re.finditer('0', puzzle)] # Find indices for all open squares in the puzzle
		for square in squares:
			possible_digits = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Can either do this, or build up a list of "excluded digits" and add the remaining digit if len(excluded) = 8. Not sure what's faster.
			for other in range(81):
				if same_row(square, other) or same_column(square, other) or same_block(square, other):
					bad_digit = int(puzzle[other])
					if bad_digit in possible_digits:
						possible_digits.remove(bad_digit)
			if len(possible_digits) == 1:
				digit = possible_digits[0]
				puzzle = puzzle[:square] + str(digit) + puzzle[square + 1:]
				replaced = True
				# print("Replaced 0 at index", square, "with", digit)
		if replaced == False: return f"Failed to solve this puzzle, here's our final position: {puzzle}"
	return puzzle
		
# print(solve(puzzles[0])) # This works! Quickly! Unfortunately, it fails for the second puzzle -- looks like they can't all be solved with process-of-elimination logic.

for i, puzzle in enumerate(puzzles):
	print(f"{i}:", solve(puzzle))

# In the end, we solve about 1/4 of the puzzles with this method. 
# If I wanted to get to the answer, the algorithm is well-known. 
# It would be easy to replicate the following: 
# https://stackoverflow.com/questions/201461/shortest-sudoku-solver-in-python-how-does-it-work

# But I'm happy with my own solution! If I wanted to go further, I could add:
# http://www.sudokuwiki.org/sudoku.htm (see "moderate puzzle" for something that uses a bit more strategy than your algorithm)

# Based on Euler forums, it looks like 4/5 of the puzzles can be solved with a "hidden singles" addition to the code, so that would be a fun extension.
# (Basically, we look at the possible digits for each cell, and if it's the only cell in a given row/column/block with that possibility, it must be right)
