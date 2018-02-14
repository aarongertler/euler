// Trying a faster variant of my solution to 23

var sumOfDivisors = function(n) {     // Returns an array with all proper divisors of n
	let sum = 0;
	for(var i = 2; i <= Math.sqrt(n); i++) { // No need to look past the square root, of course
		if(n % i === 0) {
			sum += i
			if(n / i != i) {  // No double-counting divisors for square numbers
				sum += (n / i);  
			}
		}
	}
	return sum + 1; // 1 also counts as a proper divisor
}

console.log(sumOfDivisors(28));

var abundantList = []; // array that will hold all numbers below the limit, noting whether each is abundant or not
var abundantSum = []; // array that will hold all numbers which are the sum of two abundant numbers

for(var i = 1; i < 28124; i++) {      
	if(i < sumOfDivisors(i)) {
		abundantList[i] = true
	}
}

console.log(abundantList[12])
console.log(abundantList[28])

for(var i = 1; i < 28124; i++) {
	for(var j = 1; j < i; j++) {
		if(abundantList[i] && abundantList[j]) {
			abundantSum[i + j] = true;
		}
	}
}

var sum = 0;

for(var i = 1; i < 28124; i++) {
	if(abundantSum[i] === undefined) {   // Shortest way to test whether an index value exists for an array
		sum += i
	}
}

console.log(sum)  // Yes, this is at least 10 times faster than the old version!