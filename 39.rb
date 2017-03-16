# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
# there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximised?


# Finding solutions for right triangles (a,b,c)
# Let's assume a is the longest side


def find_solutions perimeter
  solutions = []
  for b in (4...perimeter / 2)
    for a in (b + 1..perimeter / 2)
      c = perimeter - a - b
      if a ** 2 == b ** 2 + c ** 2 && b > c  # Avoid getting [50,30,40] once we've gotten [50,40,30]
        solutions << [a,b,c]
      end
    end
  end
  solutions.length
end

# puts find_solutions 30

answer = 0
highest = 0

for i in (120..1000)
  solution_count = find_solutions(i)
  if solution_count > highest
    highest = solution_count
    answer = i
  end
end

puts answer

# Ways to make this faster: Reason out some better ranges for a and b, get rid of the "c" variable