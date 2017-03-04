// A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

// Find the largest palindrome made from the product of two 3-digit numbers.




// Checks whether n is a palindrome

// var palCheck = function(n) {  
// 	n = n.toString();
// 	len = n.length;
// 	for(i = 1; i < len+1/2; i++) {
// 		// console.log(n)
// 		// console.log(i)
// 		// console.log(len)
// 		// console.log(n.substring(i-1,i))
// 		// console.log(n.substring(len-i,len-i+1))
// 		if(n.substring(i-1,i) != n.substring(len-i,len-i+1)) {
// 			return false;
// 		}
// 	}
// 	return true;
// }

// Method for checking palindromes faster (picked up from Euler after solving)

var reverse = function(n) {
	var reversed = 0
	while(n > 0) {
		reversed = 10 * reversed + (n % 10);
		n = Math.floor(n/10);
	}
	return reversed;
}
var palCheck = function(n) {
	return n === reverse(n);
}

// console.log(reverse(9001))
// console.log(palCheck(9009))


var largestPal = 0 // store the largest palindrome we've seen so far

for(var j = 100; j < 1000; j++) {
	for (k = j; k < 1000; k++) { // no need to start at k = 100, since checking 101 * 100 is redundant with checking 100 * 101
		var product = j*k;
		if(palCheck(product)) {
			if(product > largestPal) { // only add palindromes if they are they biggest we've seen so far
				largestPal = product
				// console.log(j + "*" + k + " = " + product);
			}
		}
	}
}

console.log(largestPal);


// Other ways to speed up:

// Count down from 999 instead of up from 100
// Check whether a or b is a multiple of 11 (if not, no palindrome possible)



// Unused code:

// Comparing the first half of the number to the reversed second half seemed too slow, JS has no built-in reverse function

	// firstHalf = n.substring(0, n/2)
	// console.log(firstHalf)
	// secondHalf = n.substring(n/2 + 1, n)
	// console.log(secondHalf)