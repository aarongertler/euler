// Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
// there are exactly 6 routes to the bottom right corner.

// How many such routes are there through a 20×20 grid?



var lattice = function(row,col) {
	var grid = []
	for(i = 0; i < row; i++) {
		grid[i] = [];
		for(j = 0; j < col; j++) {
			grid[i].push(0);
		}
	}
	for(i = 0; i < row; i++) {
		for(j = 0; j < row; j++) {
			if(i === 0 || j === 0) {
				grid[i][j] = 1;
			}
			else {
				grid[i][j] = grid[i-1][j] + grid[i][j-1]; // If you can get to 1,1 in two ways and 2,0 in one way, you can get to 2,1 in three ways (by stepping right from 1,1 after taking either of two paths, or stepping down from 2,0)
			}
		}
	}
	return(grid);
}

// console.log(lattice(21,21))   // 21 rows and 21 columns of lines surround a 20x20 "box" grid

// My solution simulates the lattice as an array, showing (at each "point" on the lattice) how many different steps can be taken from that path. 
// (Read the resulting lattice upside-down and left-to-right)


// How to do it faster:

// Abandon the whole matrix thing. Happily, once we know which rights we've taken, we also know exactly which downs we've taken.
// So we just need to know how many combinations of rights we can take.
// for a 20 by 20 grid, we must move right 20 times in 40 total moves. (For a 2 by 2 grid, we must move right twice in four total moves.)
// This is like flipping heads twice in four flips: There are 6 unique ways to do it (HHTT, HTHT, HTTH, THHT, THTH, TTHH)

// More generally, the formula for doing something X times in Y chances is: Y! / X!(Y-X)!  
// In our case, X and Y are the same (20 downs, 20 rights), so the math is very easy. (21/1*22/2... *40/20)

function pathNumber(length,width) {
	sum = length + width
	return factorial(sum) / factorial(length)*factorial(width)
}

function factorial(n) {
	var result = n
	while(n > 1) {
		n--
		result = result * n
	}
	return result
}

// console.log(factorial(5))
console.log(pathNumber(20,20)) // For some reason, this returns a number too large to be displayed, while the array method handled large numbers just fine...