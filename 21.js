// Let d(n) be defined as the sum of proper divisors of n (numbers less than n 
// 	which divide evenly into n).
// If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and 
// each of a and b are called amicable numbers.

// For example, the proper divisors of 220 are 
// 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
// The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

// Evaluate the sum of all the amicable numbers under 10000.


// Uncertainty: Does an amicable number count if its "partner" is greater than 10000? If a good answer is rejected, consider that possibility


// If we check numbers in 1-10000 order, we can instantly eliminate any number with divisors adding up to less than itself
// (otherwise, we'd have caught the number earlier)
// We can also eliminate all prime numbers (but how often is that faster than checking all pairs?)

var divisors = function(n) {     // Returns an array with all proper divisors of n
	var divArray = [1];
	for(var i = 2; i <= Math.sqrt(n); i++) {
		if(n % i === 0) {
			divArray.push(i);
			divArray.push(n / i);
		}
	}
	return divArray;
}

var arraySum = function(a) {
	var sum = a.reduce(function(a,b){return a+b});
	return sum
}

var amicableSum = 0;

for(var i = 1; i < 10001; i++) {
	var m = arraySum(divisors(i));
	var n = arraySum(divisors(m));
	if((i === n) && (i != m)) {
		amicableSum += i;
		console.log(i + "," + m);
	}
}

console.log(amicableSum)

// Ways to make this faster: Remove all prime numbers first?


// var genDivisorSums = function(n) {     // For all numbers up to n, create an array of pairs (number, divisor sum)
// 	var allDivArray = []
// 	for(var i = 1; i < n + 1; i++) {
// 		var divs = divisors(i)
// 		var divSum = arraySum(divs)
// 		allDivArray.push([i,divSum]);
// 	}
// 	return allDivArray;
// }

// allDivArray = genDivisorSums(10000)

// console.log(allDivArray)

// for(var i = 0; i < allDivArray.length; i++) {
// 	var first = allDivArray[i][1]
// 	var second = allDivArray[first][1]
// 	if(first = 1);
// 	else if(first === second) {
// 		resultArray.push(i)
// 		resultArray.push(first)
// 	}
// }
