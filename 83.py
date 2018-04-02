# Same as #82, but now you can go left, right, up, or down

# Rather than attack this one in the same plodding way that I did 82,
# I'm going to try adjusting Dreamshire's #82 solution to account for the extra direction.

# There's something to be learned from modifying known good algorithms, just as there is 
# from building new algorithms

# Notably, we need to end up at the bottom right

# This will actually be quite a bit different from Dreamshire, because of the bottom-right thing
# But it will be similar to a few other Eulers.
# Working backwards from the bottom-right, we want to track the lowest sum we can get away with adding to each number we find, 
# in order to get back to the bottom right

# For example, looking at the test matrix above, we'd set 956 to 956 + 331 and set 37 to 37 + 331
# Because that's the sum we'd get if we took the shortest path from each of those other numbers to 331

# ... after 90 minutes of sketching, I've determined that doing something dynamic will be really difficult, if not impossible -- there are just too many directions to look once you leave the edge of the graph
# Instead, I'm going to try and develop a graph traversal algorithm
# Dreamshire just grabbed an existing module, but let me see if I can so something from scratch.

# matrix = [[131,673,234,103,18],
#          [201,96,342,965,150],
#          [630,803,746,422,111],
#          [537,699,497,121,956],
#          [805,732,524,37,331]]

matrix = [[int(numb) for numb in line.split(',')] for line in open('p083_matrix.txt', 'r')]

from collections import defaultdict


rows, cols = len(matrix), len(matrix[0]) 

def djikstra_graph(matrix): # Set up a collection of neighbors and path lengths for each point
	graph = defaultdict(dict)
	for i in range(0, rows):
		for j in range(0, cols):
			graph[(i,j)] = {}
			if i != 0: graph[(i,j)][(i-1, j)] = matrix[i-1][j]
			if j != 0: graph[(i,j)][(i, j-1)] = matrix[i][j-1]
			if i != rows - 1: graph[(i,j)][(i+1, j)] = matrix[i+1][j]
			if j != rows - 1: graph[(i,j)][(i, j+1)] = matrix[i][j+1]
	
	return graph

# print(djikstra_graph(test_matrix))


# The below was built from http://www.gilles-bertrand.com/2014/03/dijkstra-algorithm-python-example-source-code-shortest-path.html
# But I adjusted it for this problem, fixed a couple of minor bugs, and added additional explanatory comments

# We're starting at our starting point, finding the sum of the paths from that point to its neighbors,
# and then repeating for all of our unvisited neighbor points

# At each step, we build the shortest path we can using points that are neighbors of points we've visited
# Because we're always looking to build the shortest path we can, once we hit the endpoint, we know we have a path shorter than
# any other possible path that would have started at our starting point

def shortest_path(graph, start, finish, visited = [], sums = {}, predecessors = {}):


	# Build and display the shortest path (by adding each of the predecessors we've stored to a single list)
	if start == finish:
		path = []
		pred = finish
		while pred != None:
			path.append(pred)
			pred = predecessors.get(pred,None) # Use "None" to avoid raising an error if we accidentally look for a nonexistent predecessor
		print("Shortest path:", str(path), "with a total sum of", str(sums[finish]))
		return # Once we find the shortest path, we're done

	else:
		if not visited: # We haven't looked at any nodes so far, we'll need to initialize the distance
			sums[start] = graph[(0,1)][0,0] # Grab a neighbor that will give us the value of our starting point, since that gets added to the total
		for neighbor in graph[start]:
			if neighbor not in visited:
				new_total = sums[start] + graph[start][neighbor] # Take each neighbor and check the total sum you get from taking a path to that neighbor
				if new_total < sums.get(neighbor, 10**10): # Default a very high number to check against, so that we won't accidentally set a default value if we accidentally choose a non-working neighbor
					sums[neighbor] = new_total
					predecessors[neighbor] = start # We've found that the path between our chosen neighbor value and our start value is shorter than any other path from this neighbor
					# (Remember that "start" will only be the start value once)
	visited.append(start) # Now that we've checked this node, don't run back and look at its distances again (makes sense, a shortest path will never visit the same node twice)

	# Below, we check the sums of the nodes we haven't visited yet and choose where to go next
	# Notably, the sum for any node that isn't a neighbor we've checked doesn't yet exist
	# So instead of jumping to check the smallest node on the graph, we'll check the neighbor with the shortest path connecting to it

	unvisited = {}
	for k in graph:
		if k not in visited:
			# print("K =", k, "with a sum of", sums.get(k))
			unvisited[k] = sums.get(k,10**10)

	# The below was causing an error before we added a return statement, since "unvisited" would eventually be empty
	if unvisited: # Had to add this as well
		x = min(unvisited, key = unvisited.get) # Find smallest-value node we haven't visited yet
		# print("Checking node", x, "with value", unvisited.get(x))

	shortest_path(graph, x, finish, visited, sums, predecessors)

print(shortest_path(djikstra_graph(matrix), (0,0), (rows - 1,cols - 1))) # Hits a recursion depth error on 80x80, but clearly works well for smaller matrices; I'll take it.
