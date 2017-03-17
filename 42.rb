# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); 
# so the first ten triangle numbers are:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its alphabetical position 
# and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. 
# If the word value is a triangle number then we shall call the word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly 
# two thousand common English words, how many are triangle words?


# Might as well pre-cache the most common triangle numbers (rather than doing addition for every word)

file = "p042_words.txt"
txt_string = ""
txt_string << File.read(File.open(file))
txt_array = txt_string.split(",") # Gives us an array of individual words

trim_array = []

txt_array.each do |word| 
  trim_array << word.tr("\"","")   # Trim the quotation marks from the file
end

# puts trim_array[1]


# Match all letters to their numerical values

letter_hash = Hash.new
count = 1 

for i in ("A".."Z")
  letter_hash[i] = count
  count += 1
end

# letter_hash.each { |key, val| print "#{key}: #{val} "}


triangle_array = []
sum = 0

for i in 1..25
  sum += i
  triangle_array << sum
end


triangle_count = 0

for s in (0...trim_array.length)
  word = trim_array[s]
  word_sum = 0
  for j in (0...word.length)
    word_sum += letter_hash[word[j]]
  end
  if triangle_array.include? word_sum
    triangle_count += 1
  end
end

puts triangle_count





