# It is easily proved that no equilateral triangle exists with integral length sides and integral area. 
# However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

# We shall define an almost equilateral triangle to be a triangle for which two sides are equal 
# and the third differs by no more than one unit.

# Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area 
# and whose perimeters do not exceed one billion (1,000,000,000).


# Should be fairly simple to brute-force it. But first, are there any algorithms or ideas we can borrow from other triangle problems?


# Properties of an A x A x B triangle that has an integer area: 
# Height = A^2 - (B/2)^2
# If height is even, or if B is even and height is an integer, the triangle's area is an integer

# We only need to check even values of B
# Also, A needs to be the hypotenuse of a Pythagorean triple. Let's find an algorithm to generate triples!

# Let's just go with the standard: https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple

# Note: This might not be more efficient than just checking ~two-thirds of a billion numbers (every "hypotenuse" up to a third of a billion, 
# and the non-equal sides that are one less and one greater than said hypotenuses)


limit = 10**9

# triples = []

# m = 0
# n = 0

# while m**2 + n**2 < limit / 3:

# Hold up! There's an even better sequence (need to do more Googling with these): 
# https://en.wikipedia.org/wiki/Heronian_triangle
# And of course, OEIS: https://oeis.org/A102341/internal

# The first five close-to-equilateral integer triangles have sides (5, 5, 6), (17, 17, 16), (65, 65, 66), (241, 241, 240) and (901, 901, 902).
# And technically, (1, 1, 2) also fits, though the area is 0

# What's the pattern? 17 is 4*5 - 3 (1 + 2), 65 is 4*17 - 3 (5 - 2), 241 is 4*65 - 19 (17 + 2), 901 is 4*241 - 63 (65 - 2)
# Seems like we end up referring back to the previous terms for those subtractions (and incorporating whether the previous "third side" was longer or shorter)
# Also, the "third side" is greater than the other two, then less, then greater, less, greater... (pattern continues according to OEIS)

side, last_side, side_difference, perimeter = 5, 1, 1, 16 # Start with the known triangle
total = 0

while perimeter < limit:
	side, last_side, side_difference = side * 4 - (last_side + 2*side_difference), side, -side_difference # Switch back and forth between 1 and -1 as a "side difference"
	total += perimeter # Add old perimeter before we find the new perimeter -- don't add the first perimeter over a billion
	print("Perimeter:", perimeter)
	perimeter = 3*side + side_difference # For example, since the first triangle we create is 16-17-17, side_difference is -1 and our perimeter is 50

print("Total sum:", total)


