// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

1 * 2 * 3 * 2 * 2 * 5 * 2 * 3 * 7 * 2 * 2 * 2 * 3 * 3 * 2 * 5

// If any larger number is a multiple of smaller numbers, divisible by larger = divisible by smaller

// Multiply all the primes together


// 20 is divisible by 2 and 5, no need to check those anymore
// 20 * 19 * 18 is divisible by 2, 3, 5, 6, 9, and 12

// 2^4 is last 2 factor lower than 16; 3^2 ditto; so 16 * 9 takes care of 2, 3, 4, 6, 8, 9, 12, 16
// 16 * 9 * 5 takes care of 5, 10, 15  -> all that remains is 7, 11, 13, 17, 19

factors = [];
smallestNumber = 1

var buildSmallestNumber = function(n) {
	for(var i = 2; i <= n; i++) {
		if (smallestNumber % i != 0) {
			var k = j = i;
			while(k < n/j) { // If k > n/j (that is, k is largest power of itself below n), just test k
				k = k*j;   // When we test i = 2, k winds up being 16
			}
			smallestNumber = smallestNumber * k;
			console.log("i is now " + i)
			console.log("k is now " + k)
			console.log("number is now " + smallestNumber)
		}
	}
	return smallestNumber;
}

console.log(buildSmallestNumber(20));

