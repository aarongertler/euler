// The prime factors of 13195 are 5, 7, 13 and 29.

// What is the largest prime factor of the number 600851475143?

var primes = []

// Highest number we need to check is n + 1 / largest prime so far

var primeFactors = function(n) {
	var placeholder = n; // n divided by all prime factors we've found so far
	for(var i = 2; i < Math.sqrt(placeholder); i++) {
		if(placeholder % i === 0) {
			primes.push(i);
			// console.log("This prime: " + i)
			placeholder = placeholder / i;
			// console.log("New placeholder: " + placeholder)
			i--
		}
	}
	return placeholder // once we've checked all numbers below sqrt(placeholder), placeholder must be the last prime (see below)
}

// console.log(primeFactors(48000))

var largestPrime = function(n) {
	console.log(primeFactors(n));
	// var last = primes.length - 1;
	// return primes[last];
}

// var test = (3*5*7*11*13*17*19*23*29*31*37*41*43)
	// Fun fact: If you test with the above number * 47, it becomes too large for JS to work with properly!
	// JS rounds off to a strange number with, I assume, an enormous greatest prime factor (because the calculation stalls out for a while)
// var test = (2*2*2*2*2*2*2*2*2*2*2*2*2*2*22*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*1024*1024)
	// But this still works, since we can always divide by 2 or 11
// console.log(test)
// console.log(largestPrime(13195))
console.log(largestPrime(600851475143))



// Ways to speed this up:

// Check 2 separately, then i+=2 instead of i++ (if 2 isn't a factor, neither is 4, 6, etc.)
// Only check factors <= the square root of placeholder
	// e.g. for 2 * 3 * 37 * 41, once we divide out 2 and 3, 
	// we know that there can be only one factor greater than sqrt(37 * 41)
	// and once we divide out 37, only one factor greater than sqrt(41)
	// once we get past 6, 41 is the only possible factor left (anything else would imply we missed a factor earlier)
// Actually, I went back and implemented the second part, just for fun!
