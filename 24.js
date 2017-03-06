// A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
//If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
// The lexicographic permutations of 0, 1 and 2 are:

// 012   021   102   120   201   210

// What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?



// We can quickly "zoom in" on the millionth set of digits

// There are 10! =/= 3.6 million permutations. The first digit of the first 0.36 million will be 0. The first digit of the 1 millionth will be 2.
// (This is equal to 1m / 10! % 10)
// There are 9! (10!/10) combinations that start with 2. The first of these is permutation # 2(9!)+1. The last is permutation #3(9!).
// 2 * 9! + 1 = 725761. 3 * 9! = 1088640. The difference is 9! (362880). The 1 millionth permutation is 1m - 725760  into this "gap".

// The pattern: 1000000 = a*9! + b*8! + c*7!... + 1, where a = 2, b = the second digit, and so on. (I think, will have to build it out and see
// if it still makes sense)

// Though we have to account for digits that go missing

var factorial = function(n) {          // n is a string; to get 100!, enter "100"
	value = 1;
	for(var i = 2; i < parseInt(n) + 1; i++) {   // Remember to re-declare loop variables!
		value = value*i
	}
	return value;
}

// console.log(factorial(8));


numValues = factorial(10) // number of possible combinations of 10 unique digits
permutation = 1000000; // the number of the permutation we are looking for
available = [0,1,2,3,4,5,6,7,8,9] // digits that could be "next"
digits = [];

for(var i = 9; i > -1; i--) {
	digit = 0;
	while(permutation > factorial(i)) {
		permutation -= factorial(i);
		digit++
	}
	index = digit // Gets us the right "distance" down the set of digits we have (pick the xth-largest, where x is the number of factorials "down the gap" we are)
	digit = available[digit];
	available.splice(index,1)
	digits.push(digit);
}

console.log(permutation);
console.log(digits);
