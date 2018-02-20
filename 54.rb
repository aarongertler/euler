# In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

# If two players have the same ranked hands then the rank made up of the highest value wins; 
# for example, a pair of eights beats a pair of fives (see example 1 below). 
# But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); 
# if the highest cards tie then the next highest cards are compared, and so on.

# The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

# How many hands does Player 1 win?

# require 'math'

file = "p054_poker.txt" # Let's break this file into a set of 1000 hands (each hand is an array of two arrays)

hand_string = ""
hand_string << File.read(File.open(file))
hand_array = hand_string.split(" ")

hands = Array.new # Nested array: Hands[5][1] will contain the second player's hand in the fifth game

for i in (0..9999)
	hand_count = (i / 10).floor
	if i % 10 == 0
		hands << [[],[]] # Initializing this array was tricky for some reason -- I was very rusty on my nesting
	end
	if i % 10 < 5
		hands[hand_count][0] << hand_array[i]
	else
		hands[hand_count][1] << (hand_array[i])
	end
end

# print hands[400]



# txt_array.each do |word| 
#   trim_array << word.tr("\"","")   # Trim the quotation marks from the file
# end