// A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
// For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

// A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

// As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
// By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
// However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number 
// that cannot be expressed as the sum of two abundant numbers is less than this limit.

// Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


// Very similar to 21.js! Let's grab a list of all abundant numbers first:

var divisors = function(n) {     // Returns an array with all proper divisors of n
	var divArray = [1];
	for(var i = 2; i <= Math.sqrt(n); i++) {
		if(n % i === 0) {
			divArray.push(i);
			if(n / i != i) {
				divArray.push(n / i);  // No double-counting divisors for square numbers
			}
		}
	}
	return divArray;
}

var arraySum = function(a) {
	var sum = a.reduce(function(a,b){return a+b});
	return sum
}

var abundantList = [];

for(var i = 1; i < 28124; i++) {      
	var m = arraySum(divisors(i));
	if(i < m) {
		abundantList.push(i);
	}
}

// console.log(abundantList); 

var allNums = [];     // Holds all numbers between 1 and 28123

for(var i = 1; i < 28124; i++) {
	allNums.push(i);
}

// console.log(allNums)

for(var i = 0; i < abundantList.length; i++) {
	for(var j = i; j < abundantList.length; j++) {     // Once we've added a + b, no need to add b + a
		var sum = abundantList[i] + abundantList[j];
		var index = allNums.indexOf(sum);
		if(index !== -1) {
			allNums.splice(index,1);
		}
	}
}

// console.log(allNums);

var nonSums = arraySum(allNums);     // We've knocked all abundant sums out of AllNums, whatever's left should count

console.log(nonSums);

// for(var i = 0; i < 28124; i++) {
// 	if(allSums.indexOf(i) === -1) {
// 		nonSums += i;
// 		console.log(i)
// 	}
// }

// console.log(nonSums);

