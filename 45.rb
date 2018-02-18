# Triangle    Tn=n(n+1)/2   1, 3, 6, 10, 15, ...
# Pentagonal    Pn=n(3n−1)/2    1, 5, 12, 22, 35, ...
# Hexagonal   Hn=n(2n−1)    1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755.

# Find the next triangle number that is also pentagonal and hexagonal.

def is_pentagonal n
  ((Math.sqrt(24 * n + 1) + 1) / 6) % 1 == 0   # Wound up just grabbing this from Wikipedia
end

# Fun fact: If, for triangular numbers, we turn n into 2n - 1, 
# triangular numbers turn into hexagonal numbers!
# (2n - 1)(2n - 1 + 1) / 2 = (2n - 1)2n / 2 = 2n(n - 1)

# Thus, H(3) = T(5), H(4) = T(7), and so on

flag = false # Avoiding a long "until" statement with this "flag" workaround, I think it makes the code a bit cleaner to read

count = 285 # Our defined starting point

until flag == true
  count += 1
  tri_n = (count * (count + 1)) / 2
  if tri_n % 2 != 0 && is_pentagonal(tri_n) # As noted above, all triangular numbers with an odd "n" seed are also hexagonal
    puts tri_n
    flag = true
  end
end