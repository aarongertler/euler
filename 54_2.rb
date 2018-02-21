$card_rankings = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]

$hand_rankings = [[1,1,1,1,1],[2,1,1,1],[2,2,1],[3,1,1],[],[],[3,2],[4,1]] # Blank spaces represent flushes and straights 

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

def get_cards hand # This can be done in one line in Python -- probably could be shortened here, as well?
	cards = Array.new
	for i in 0..4
		cards << $card_rankings.index(hand[i][0]) + 2  # Add two so that we value "2" as 2, "A" as 14
	end
	cards
end

def get_suits hand
	suits = Array.new
	for i in 0..4
		suits << hand[i][1]
	end
	suits
end

def check_straight hand
	sorted = get_cards(hand).sort
	if (sorted[0] == (sorted[4] - 4)) && sorted.uniq.length == 5 # No duplicates, and the value of the lowest card is "4 less" than the value of the highest card
		return true
	end
	false
end

def check_flush hand
	get_suits(hand).uniq.length == 1
end

def get_frequencies cards
	# For each key we run across (e.g. "8", add 1 to the value for that key (so we get a value of 2 for "8" if we have two eights))
	cards.each_with_object(Hash.new(0)){ |m,h| h[m] += 1 }.sort_by{ |k,v| v*15 + k }.reverse # Make sure that we sort the highest, most frequent cards to the front of the list
end

def hand_rank hand
	freq = get_frequencies(get_cards(hand))
	ranking = freq.map {|x| x.pop}
	score = $hand_rankings.index(ranking).to_f
	if check_straight(hand)
		score = 4
	elsif check_flush(hand)
		score == 4 ? score = 8 : score = 5
	end
	values = freq.map {|x| x.shift}
	for i in 0..values.length - 1
		score += (values[i].to_f / 15 ** (i + 1)) # Guarantees that the highest card in a hand is worth more than the rest, allows for perfect tiebreaking
	end
	score
end

total = 0 

for i in 0..999
	hand_1 = hands[i][0]
	hand_2 = hands[i][1]
	if hand_rank(hand_1) > hand_rank(hand_2)
		total += 1
	end
end

puts total # Got it! Just had to sort the hands correctly, in the end.


# Inspired by the beautiful Python below, from https://blog.dreamshire.com/project-euler-54-solution/

# values = {r:i for i,r in enumerate('23456789TJQKA', 2)}
# straights = [(v, v-1, v-2, v-3, v-4) for v in range(14, 5, -1)] + [(14, 5, 4, 3, 2)]
# ranks = [(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(),(),(3,2),(4,1)]

# def hand_rank(hand):
# 	score = zip(*sorted(((v, values[k]) for
# 		k,v in Counter(x[0] for x in hand).items()), reverse=True))
# 	score[0] = ranks.index(score[0])
# 	if len(set(card[1] for card in hand)) == 1: score[0] = 5  # flush
# 	if score[1] in straights: score[0] = 8 if score[0] == 5 else 4  # str./str. flush
# 	return score

# print "P1 wins", sum(hand_rank(hand[:5]) > hand_rank(hand[5:]) for hand in hands)