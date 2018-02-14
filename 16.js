// 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

// What is the sum of the digits of the number 2^1000?

// console.log(Math.pow(2,1000)) // Too big!

// Can we find a pattern?

// 2^1 = 2, 2^2 = 4, 2^3 = 8, 2^4 = 7, 2^5 = 5, 2^6 = 10, 2^7 = 11, 2^8 = 13, 2^9 = 8, 2^10 = 7... no clear pattern

var bigInt = require("big-integer"); // https://github.com/peterolson/BigInteger.js

var bigNumber = bigInt(Math.pow(2,50))
// var bigNumber = bigNumber.toString()

var digitSum = function(n) {
	sum = 0
	n = n.toString()
	len = n.length
	for(i = 0; i < len; i++) {
		sum += parseInt(n.substring(i,i+1));
	}
	return sum;
}

var bigString = (bigNumber.toString())
console.log(bigString)
console.log(digitSum(bigNumber))


// Behold, a horrifically ugly function. 
// If I were more disciplined, I'd write a generalized "times x" function or something.
// But alas, I am not. (Though problem 20 requires this, so I did the better function in 20.js)

var timesTwo = function(array) {
	len = array.length;
	for(i = 0; i < len; i++) {
		if(array[i]*2 >= 10) {
			if(i === 0) {
				array.unshift(1)
				len++
				array[i+1] = (array[i+1]*2 % 10)
				i++
			}
			else {
				array[i-1] = array[i-1] + 1
				array[i] = (array[i]*2 % 10)
			}
		}
		else {
			array[i] = array[i]*2;
		}
	}
	return array;
}

// var test = [4,0,9,6]
// console.log(timesTwo([3,2]))

var power = [2]

for(j = 1; j < 1000; j++) {
	power = timesTwo(power)
}

var sum = power.reduce(function(a,b){return a+b});

// console.log(power)
console.log(sum)