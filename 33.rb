# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting 
# to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than one in value, 
# and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

solutions = []

for i in (11..99)
  if i % 10 == 0
    then next
  else
    for j in (i+1..99)  # j > i, since the fraction is less than one
      if j % 10 == 0
        then next
      else
        i = i.to_s
        j = j.to_s
        a = i.delete(j).to_f
        b = j.delete(i).to_f
        if a < 10 && b < 10
          if a / b == i.to_f / j.to_f
            solutions.push([i.to_f,j.to_f])
          end
        end
      end
    end
  end
end

puts solutions

solutions = solutions.flat_map { |n| n[0] / n[1]}  # Get everything in simplified form for easy multiplication
puts solutions 

# Ways to do this faster: Assemble all the fractions yourself (for a and b in 1...10, a*10 + b / b*10 + a), though since we skip multiples of 10 I doubt that would add much speed
# in general, all the other solutions seem broadly similar, no crazy one-liners