// The sum of the squares of the first ten natural numbers is,

// 1^2 + 2^2 + ... + 10^2 = 385
// The square of the sum of the first ten natural numbers is,

// (1 + 2 + ... + 10)^12 = 55^2 = 3025
// Hence the difference between the sum of the squares of the first ten 
// natural numbers and the square of the sum is 3025 − 385 = 2640.

// Find the difference between the sum of the squares of the first one hundred natural numbers 
// and the square of the sum.


// This one is really straightforward, not going to bother turning it into a function

var sum = 0;

for(i = 1; i < 101; i++) {
	sum += i;
}

console.log(sum*sum)

var sumSquares = 0

for(i = 1; i < 101; i++) {
	sumSquares += i*i
}

console.log(sumSquares)

console.log(sum*sum - sumSquares)


// Doing it better, with math to adjust to any limit

// Sum of squares: f(n+1) = f(n) + (n+1)^2
// Add 1 inside the function, add (n+1)^2 overall = add (n^2 + 2n + 1) overall
// f(n) = f(n-1) + n^2 + 2n + 1 = n(n + 2 + 1/n) = add n(n + 2) + 1
// f(n) = ax^3 + bx^2 + cx + d
// 64a + 16b + 4c + d = 30
// 27a + 9b + 3c + d = 14
// 8a + 4b + 2c + d = 5
// a + b + c + d = 1

// Eliminate c: 60a + 12b - 3d = 26
//              24a + 6b - 2d = 11
//              6a + 2b - d = 3

// Eliminate b: 6a + d = 2
//              24a + 3d = 8

// Eliminate d: 6a = 2    a = 1/3    d = 0    b = 1/2    c = 1/6
// f(n) = 1/3(x^3) + 1/2(x^2) + 1/6(x) = (2x^3 + 3x^2 + x)/6 = x(2x^2 + 3x + 1)/6 = x(2x + 1)(x + 1)/6

// f(0) = 0
// f(1) = 1 = (3)(2)(1/6)
// f(2) = f(1) + 4 = 5 = (5)(3)(2/6)
// f(3) = f(2) + 9 = 14 = (7)(4)(3/6)
// f(4) = f(3) + 16 = 30 = (9)(5)(4/6)
// f(5) = 55 = (11)(6)(5/6)
// f(6) = 91 = (13)(7)(6/6)

var sumSquares = function(x) {
	return (2*x + 1)*(x + 1)*(x/6)
}

var squareSum = function(x) {
	sum = (x + 1)*(x/2)   // basic rule of sums (for 1 to 100, add 1 to 100, then add 2 to 99... for 50*101)
	return sum*sum
}

console.log(squareSum(1000000) - sumSquares(1000000)) // very quick!