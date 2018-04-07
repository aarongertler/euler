# What are the three squares you'll most often end on if you play Monopoly with two four-sided dice?

# I could either look at this mathematically or run a simulation with 10,000 rolls or so. Let's go with the second,
# which will take longer, but also be more flexible for different types of board games (and easier to read).

# For now, I'll ignore the order of cards in the CC/CH decks: Because we're 
# moving so frequently around, we'll see all the cards a huge number of times, making the first one we see irrelevant


from random import randint
from collections import defaultdict
from operator import itemgetter

board = ["GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3", "JAIL",
					"C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3", "FP", "E1",
					"CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3", "G2J", "G1", "G2",
					"CC3", "G3", "R4", "CH3", "H1", "T2", "H2"]

chance_cards = ["GO", "JAIL", "C1", "E3", "H2", "R1", "NEXT_R", "NEXT_R", 
								"NEXT_U", "BACK_3", "", "", "", "", "", ""]

community_cards = ["GO", "JAIL", "", "", "", "", "", "", "", ""]

end_pos = len(board)
chance_count = len(chance_cards)
community_count = len(community_cards)

end_squares = defaultdict(int)

def move(die_1, die_2, board, position, count): # For a four-sided die, set die_1 = 4
	moves = 0
	doubles = 0
	while moves < count:
		first_roll, second_roll = randint(1, die_1), randint(1, die_2)
		if first_roll == second_roll: 
			doubles += 1
		else:
			doubles = 0 # Was getting wrong answer until I remembered to reset my doubles count
		if doubles == 3: # 3 doubles in a row, go to jail
			square, position = "JAIL", 10
			doubles = 0
		else:
			roll = first_roll + second_roll
			position += roll
			if position >= end_pos: position = position % end_pos # We've reached the end of the board, double back to the starting point
			if board[position] not in ["G2J", "CC1", "CC2", "CC3", "CH1", "CH2", "CH3"]:
				square = board[position]
			else: # We've hit a square that could send us somewhere else
				square = final_square(board, position)
			position = board.index(square) # Got the wrong answer at first, when I neglected to adjust positions to account for position movement on CC, CH, and G2J cards (squares and positions should line up)
		end_squares[square] += 1
		moves += 1
		# print("Rolled a", roll, ", now at square", square, "in position", position)

def final_square(board, position):
	start_square = board[position]
	if start_square == "G2J":
		return "JAIL"
	elif start_square in ["CH1", "CH2", "CH3"]:
		card = chance_cards[randint(0, chance_count - 1)]
		if card == "":
			return start_square
		elif card in ["GO", "JAIL", "C1", "E3", "H2", "R1"]:
			return card
		elif card == "NEXT_R":
			if start_square == "CH1":
				return "R2"
			if start_square == "CH2":
				return "R3"
			else:
				return "R1"
		elif card == "NEXT_U":
			if start_square in ["CH1", "CH3"]:
				return "U1"
			else:
				return "U2"
		elif card == "BACK_3":
			return board[position - 3]
	else: # Not G2J or chance, must be community
		card = community_cards[randint(0, community_count - 1)]
		if card == "":
			return start_square
		else: # Card is "GO" or "JAIL"
			return card


move(4, 4, board, 0, 100000) # This works to get the first and second-most common squares consistently.
	# The third-most common square is practically a tie, but one of the tied answers works (not sure whether my code is wrong somewhere for things to be so close)
	# This code takes about 10 seconds for two million rolls, which is serviceable

sorted_squares = sorted(end_squares.items(), key=itemgetter(1), reverse=True)
print(sorted_squares)


# Ways to make this faster/smoother:

# Build an actual probability matrix instead of sticking to the "board" structure
	# This will let you use Markov chains, which should be considerably quicker 


# As expected, the Euler solution thread is half posts complaining about different interpretations of the rules,
# and people have hit many different sets of percentages. Board games are tough!