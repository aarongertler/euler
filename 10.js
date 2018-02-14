// Find the sum of all primes below 2 million

var checkNum = 3 // The number we're checking for prime-ness
var primeArr = [2] // An array which holds our primes (starts with 2 and 3 inside)

var primeBelowN = function(n) {
	var len = primeArr.length
	while(checkNum < n) {
		var i = 0 // loop back to the beginning of the prime array
		var isPrime = true
		while(primeArr[i] < Math.sqrt(checkNum)) { // Loop through our array of known primes until we hit one that divides our number
			if(checkNum % primeArr[i] === 0) { // This prime divided the number we're checking, it can't be prime
				i = primeArr.length // break out of the loop
				isPrime = false
			} 
			else {
				i++
			}
		} 
		if(isPrime) {
			primeArr.push(checkNum);  // no primes in our array worked, so this number is prime!
			// console.log(checkNum + " is prime!")
			var len=primeArr.length
		}
		checkNum += 2; // check the next odd number
	}
	console.log(primeArr[len-1]);
	var sum = primeArr.reduce(function(a,b){return a+b});
	console.log(sum);
}

console.log(primeBelowN(2000000))



// Wikipedia offers some good pseudocode for skipping every third number check: https://en.wikipedia.org/wiki/Primality_test
// The page also has some good heuristics for checking any *practical* range of primes (even if said heuristics are unproven)

// Euler suggests a sieve algorithm where you start with an array of two million numbers, then cut them off as you go. That goes much faster!