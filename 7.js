// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

// What is the 10001st prime number?



// Start with simple brute-force algorithm to get the gears turning... (and it turns out brute force is enough)

var numPrime = 1  // The number of primes we've found. We start having already "found" the number 2.
var checkNum = 3 // The number we're checking for prime-ness
var primeArr = [2] // An array which holds our primes (starts with 2 inside)

var nthPrime = function(n) {
	while(numPrime < n) {
		var i = 0 // loop back to the beginning of the prime array
		var isPrime = true
		while(i < primeArr.length) { // Loop through our array of known primes until we hit one that divides our number
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
			console.log(checkNum + " is prime!")
			numPrime++
		}
		checkNum += 2; // check the next odd number
	}
	console.log(primeArr[n-1])
}

console.log(nthPrime(10001))


// How to make this faster: As with Euler Problem 3, only check factors below sqrt(number) -- if none of those work, the number is prime
// Also, it's not too hard to skip every multiple of 3 and every multiple of 5 if you want to boost performance