# Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). 
# For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

# A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, 
# taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, 
# restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

# For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. 
# The user would keep the encrypted message and the encryption key in different locations, and without both "halves", 
# it is impossible to decrypt the message.

# Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. 
# If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. 
# The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

# Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher.txt, 
# a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, 
# decrypt the message and find the sum of the ASCII values in the original text.

require 'xorcist'

# Basic cryptography rule: Find the most common character --> if this is a real message, it should be a space

file = "p059_cipher.txt"
cipher_array = File.read(File.open(file)).split(',')
first, second, third = [], [], []


# print cipher_array

for i in (0..cipher_array.length - 1).step(3) do # Key is three characters, so we want to find a separate decryption key for each third of the message
	first << cipher_array[i]
	second << cipher_array[i + 1]
	third << cipher_array[i + 2]
end

freq = [] # Stores the most common character for each third of the message

# The below could be simplified to eliminate repetition if I wanted to improve readability

freq[0] = first.each_with_object(Hash.new(0)){ |m,h| h[m] += 1 }.sort_by{ |k,v| v }.reverse # Put most common character in front
freq[1] = second.each_with_object(Hash.new(0)){ |m,h| h[m] += 1 }.sort_by{ |k,v| v }.reverse # Put most common character in front
freq[2] = third.each_with_object(Hash.new(0)){ |m,h| h[m] += 1 }.sort_by{ |k,v| v }.reverse # Put most common character in front

print freq[0][0], freq[1][0], freq[2][0] # "79", "68", and "71" are the spacebar characters (we'll assume for now)

key = []
message = []
space_ascii = 32 # Value of the spacebar key in ASCII: https://ascii.cl/

for i in 0..2
	key[i] = freq[i][0][0].to_i ^ space_ascii # 100, 111, 103 --> "g", "o", "d"
end

for i in 0..cipher_array.length - 1
	message[i] = cipher_array[i].to_i ^ key[i % key.length]  # Decrypt the first character with key[0], the next with key[1], etc.
end

print message.reduce(0, :+)


# I had no idea what was going on here, and Ruby doesn't seem well-tuned to ASCII -- I'm still not sure what the best way is to turn my message 
# array full of numbers into an actual message. But the sum is acccurate, at least.

# Wouldn't have been able to make heads or tails of this without seeing: http://www.mathblog.dk/project-euler-59-xor-encryption/