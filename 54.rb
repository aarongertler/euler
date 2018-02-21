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

# The file, poker.txt, contains one thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

# How many hands does Player 1 win?



# First attempt: Not trying to minimize code, instead trying to optimize for readability
# In the end, something went wrong, and I've misclassified a tiny % of hands (though it's very hard to tell where)

# require 'facets' # Not using "frequency" to sort our card frequencies anymore

$card_rankings = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"] 

file = "p054_poker.txt" # Let's break this file into a set of 1000 hands (each hand is an array of two arrays)

hand_string = ""
hand_string << File.read(File.open(file))
hand_array = hand_string.split("\n")

hands = Array.new

for i in 0..999
	hands << [[],[]]
	hand_array[i] = hand_array[i].split(" ")
	hands[i][0] = hand_array[i][0,5]
	hands[i][1] = hand_array[i][5,9]
end

# print hands[400]

def get_suits hand
	suits = Array.new
	for i in 0..4
		suits << hand[i][1]
	end
	suits
end

def get_cards hand
	cards = Array.new
	for i in 0..4
		cards << $card_rankings.index(hand[i][0]) + 2  # Add two so that we value "2" as 2, "A" as 14
	end
	cards
end

def check_straight hand
	sorted = get_cards(hand).sort
	if (sorted[0] == (sorted[4] - 4)) && sorted.uniq.length == 5 # No duplicates, and the value of the lowest card is "4 less" than the value of the highest card
		return true
	end
	false
end

def get_frequencies cards
	cards.each_with_object(Hash.new(0)){ |m,h| h[m] += 1 }.sort_by{ |k,v| v*15 + k }.reverse # Make sure that we sort the highest, most frequent cards to the front of the list
end

def hand_type hand  # Determine which type of hand the player has
	flush, straight = nil, nil
	suits = get_suits(hand)
  cards = get_cards(hand)
	freq = get_frequencies(cards)
	if suits.uniq.length == 1
		flush == true
	end
	if check_straight(hand) == true
		straight == true
	end
	if flush == true
		if straight == true
			if cards.include?(14) # That is, if your straight has an ace in it
 				return "Royal Flush"
			end
			return ["Straight Flush", cards]
		end
		return ["Flush", cards]
	end
	if freq[0][1] == 4
		return ["Four of a Kind", freq[0][0], freq[1][0]]
	end
	if freq[0][1] == 3 && freq[1][1] == 2
		return ["Full House", freq[0][0], freq[1][0]]
	end
	if straight == true
		return ["Straight", cards]
	end
	if freq[0][1] == 3
		return ["Three of a Kind", freq[0][0], cards.delete_if {|x| x == freq[0][0] }]
	end
	if freq[0][1] == 2 && freq[1][1] == 2
		return ["Two Pair", freq[0][0], freq[1][0], freq[2][0]]
	end
	if freq[0][1] == 2
		return ["One Pair", freq[0][0], cards.delete_if {|x| x == freq[0][0] } ]
	end
	["High Card", cards]
end

def hand_value hand
	type = hand_type(hand)[0]
	case type
	when "Royal Flush"
		return 10
	when "Straight Flush"
		return 9
	when "Four of a Kind"
		return 8
	when "Full House"
		return 7
	when "Flush"
		return 6
	when "Straight"
		return 5
	when "Three of a Kind"
		return 4
	when "Two Pair"
		return 3
	when "One Pair"
		return 2
	when "High Card"
		return 1
	end
end

def compare_hands hand_1, hand_2
	if hand_value(hand_1) > hand_value(hand_2)
		return "P1"
	elsif hand_value(hand_2) > hand_value(hand_1)
		return "P2"
	else
		return break_tie(hand_1, hand_2)
	end
end

def break_tie hand_1, hand_2
	case hand_type(hand_1)[0]
	when "Four of a Kind"
		result = compare(hand_type(hand_1)[1], hand_type(hand_2)[1])
		if result == "Tie"
			result = compare(hand_type(hand_1)[2], hand_type(hand_2)[2])
		end
		result
	when "Three of a Kind"
		result = compare(hand_type(hand_1)[1], hand_type(hand_2)[1])
		if result == "Tie"
			result = batch_compare(hand_type(hand_1)[2], hand_type(hand_2)[2]) # Holds the cards that weren't in our three-of-a-kind
		end
		result
	when "One Pair"
		result = compare(hand_type(hand_1)[1], hand_type(hand_2)[1])
		if result == "Tie"
			result = batch_compare(hand_type(hand_1)[2], hand_type(hand_2)[2]) # Holds the cards that weren't in our pair
		end
		result
	when "Full House"
		result = compare(hand_type(hand_1)[1], hand_type(hand_2)[1])
		if result == "Tie"
			result = compare(hand_type(hand_1)[2], hand_type(hand_2)[2])
		end
		result
	when "Two Pair"
		result = compare(hand_type(hand_1)[2], hand_type(hand_2)[2]) # Second pair will have the higher numbers
		if result == "Tie"
			result = compare(hand_type(hand_1)[1], hand_type(hand_2)[1]) # First pair will have the lower numbers
			if result == "Tie"
				result = compare(hand_type(hand_1)[3], hand_type(hand_2)[3])
			end
		end
		result
	when "Straight", "Straight Flush" # Compare the highest card in each hand
		compare(
			get_cards(hand_1).sort[0], 
			get_cards(hand_2).sort[0]
			) 
	when "Flush", "High Card" # Compare all the cards until we can break a tie
		batch_compare(get_cards(hand_1), get_cards(hand_2))
	end
end

def batch_compare cards_1, cards_2 
	sorted_1 = cards_1.sort.reverse # Compare the highest cards first!
	sorted_2 = cards_2.sort.reverse
	i = 0
	result = "Tie"
	until result != "Tie" || i == cards_1.length - 1 # Stop comparing if someone wins or we run out of cards
		result = compare(sorted_1[i], sorted_2[i])
		i += 1
	end
	result
end

def compare first_card, second_card
	if first_card > second_card
		return "P1"
	elsif second_card > first_card
		return "P2"
	else
		return "Tie"
	end
end

total = 0 

for i in 0..999
	hand_1 = hands[i][0]
	hand_2 = hands[i][1]
	# print hand_type(hand_1)[0]
	# puts " " + hand_type(hand_2)[0]
	# puts compare_hands(hand_1, hand_2)
	if compare_hands(hand_1,hand_2) == "P1"
		total += 1
	end
end

puts total # Off by 3 hands here, for some reason -- very hard to detect why, since manual checks of the first 50 hands looked good



