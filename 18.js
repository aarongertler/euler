// By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

// 3
// 7 4
// 2 4 6
// 8 5 9 3

// That is, 3 + 7 + 4 + 9 = 23.

// Find the maximum total from top to bottom of the triangle below:

// 75
// 95 64
// 17 47 82
// 18 35 87 10
// 20 04 82 47 65
// 19 01 23 75 03 34
// 88 02 77 73 07 63 67
// 99 65 04 28 06 16 70 92
// 41 41 26 56 83 40 80 70 33
// 41 48 72 33 47 32 37 16 94 29
// 53 71 44 65 25 43 91 52 97 51 14
// 70 11 33 28 77 73 17 78 39 68 17 57
// 91 71 52 38 17 14 91 43 58 50 27 29 48
// 63 66 04 68 89 53 67 30 73 16 69 87 40 31
// 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

// NOTE: The triangles are actually equilateral, not right, so every number has two adjacent numbers below, not three                                       

var smallTriangle = "08 \
65 62 \
14 85 99 "


var bigTriangle = "75 \
95 64 \
17 47 82 \
18 35 87 10 \
20 04 82 47 65 \
19 01 23 75 03 34 \
88 02 77 73 07 63 67 \
99 65 04 28 06 16 70 92 \
41 41 26 56 83 40 80 70 33 \
41 48 72 33 47 32 37 16 94 29 \
53 71 44 65 25 43 91 52 97 51 14 \
70 11 33 28 77 73 17 78 39 68 17 57 \
91 71 52 38 17 14 91 43 58 50 27 29 48 \
63 66 04 68 89 53 67 30 73 16 69 87 40 31 \
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23 "



var numberOfRows = function(n) {   // determine the number of rows in a triangle with n numbers
	var rows = 0;
	var subtract = 1;
	while(n > 0) {
		n -= subtract;
		subtract++; // First row has one number, second has two numbers, etc.
		rows++;
	}
	return(rows);
}

var createArray = function(s) {   // turn a string of two-digit numbers into an array of numbers
	var array = [];
	for(i = 0; i < s.length / 3; i++) {
		array.push(parseInt(s.substring(i*3,(i+1)*3))); // parseInt converts a string into a number
	}
	return array;
}

console.log(createArray("06 14 19 "))

var loadTriangle = function(a) {  // turn a single array into a "triangular" array full of sub-arrays
	var numberOfNumbers = a.length;
	var rowCount = numberOfRows(numberOfNumbers);
	var triangle = [];
	var k = 0;    // tracks which number of our full array we're pushing into the row next (1 for first row, 2-3 for second, etc.)
	for(i = 0; i < rowCount; i++) {
		triangle[i] = [];   // Initialize a new "row" of the triangle
		for(j = 0; j < i + 1; j++) {
			triangle[i].push(a[k]);
			k++
		}
	}
	return triangle;
}

// console.log(createArray(bigTriangle).length)
// console.log(numberOfRows(createArray(bigTriangle).length))
console.log(loadTriangle(createArray(smallTriangle)))
console.log(loadTriangle(createArray(bigTriangle)))

var triangulate = function(s) {   // Sandwich both of our triangle-making functions together for convenience
	return loadTriangle(createArray(s));
}

console.log(triangulate(smallTriangle).reverse());

// Okay! We've successfully crafted a triangle. Now what?
// We don't want to just brute-force this, since Euler #67 gives us a triangle too large to brute-force.

// First idea: Measure the first path, then stop tracking any subsequent path when it becomes clear 
// that path won't lead to as large a sum as our biggest path so far

// Seems fine, but maybe not recursive enough? We'd still be running through a lot of half-finished paths...

// Second idea: Experiment with recursion. First, invert the triangle. Then ask: 
// What's the highest value we can reach at number n in row x? Answer: n + the max of the same question for the two 
// adjacent numbers in row x-1. (Does this count as dynamic programming?)

var testArray = triangulate(bigTriangle).reverse() // Invert the triangle, since we want to go "from the bottom, up"

var spotMax = function(tri,a,b) {     // for the b-th number in the a-th row of a triangle, what is the max value we can have upon reaching it?
	if(b < 0) {
		return 0;   // We can't check the spotmax of this number, because it doesn't exist
	}
	if(a === 0) {  // We're on the last row, recursion over
		return tri[a][b];
	}
	else {
		return tri[a][b] + Math.max(spotMax(tri,a-1,b), spotMax(tri,a-1,b+1))   // spotMax(a,4,0) = a[4][0] + whichever spotMax is highest from (a,3,0) and (a,3,1)
	}
}

console.log(spotMax(testArray,testArray.length-1,0))   // But is this really faster? Simpler, yes, but faster?


// That works! Now to see if it will work for 67... (it did) (also, some neat visuals in the solution thread, of what the sums look like for every point in the triangle)
