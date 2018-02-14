// By considering the terms in the Fibonacci sequence 
// whose values do not exceed four million, find the sum 
// of the even-valued terms.


// Fibonacci function #1: Elegant, but very slow

// var fib = function(n) {
// 	if (n < 2) {
// 		return 1;
// 	}
// 	else {
// 		return(fib(n-1) + fib(n-2))
// 	}
// }


// Fibonacci function #2: Non-recursive, but fast enough for the Euler problem (if I insist on adding a separate function)

// var n = 10   // This gets us the 10th Fibonacci number (where '0' is the first)
// var fib = function(n) {
// 	var sum1 = 0 // since we're running this function repeatedly below, these can't be global
// 	var sum2 = 1
// 	if(n < 2) {
// 		return 0
// 	}
// 	for(var i = 0; i < n - 3; i++) {
// 		if(i % 2 === 0) {
// 			sum1 += sum2;
// 		} // doing this with just two holding variables for fun, 3 is easier
// 		else {
// 			sum2 += sum1;
// 		}
// 	}
// 	return(sum1 + sum2)
// }

// var x = 0;
// var fibVal = 0;
// var fibSum = 0;
// var limit = 4000000;

// while(fibVal <= limit) {
// 	x++
// 	fibVal = fib(x)
// 	if(fibVal % 2 === 0) {
// 		fibSum += fibVal
// 		console.log(fibVal)
// 	}
// } console.log(fibSum)

// Function 3: Recursive, so should be quite a bit faster:

var fibOne = 0;
var fibTwo = 1;
var fibThree = 1;
var fibSum = 0;
var limit = 4000000;

while(fibThree <= limit) {
	fibThree = fibOne + fibTwo;
	fibOne = fibTwo;
	fibTwo = fibThree;
	if(fibThree % 2 === 0) {
		fibSum += fibThree
		console.log(fibThree)
	}
} console.log(fibSum)



// The above works! Here's a quick way to do it if you don't actually want a separate Fibonacci function:

// Courtesy of https://rajat-dhyani.github.io/project_euler/

// function q2Calc(){
// 		var no = 4000000
// 		var a = 0;
// 		var b  = 1;
// 		var c = 1;
// 		var sum = 0;
// 		while( c <= no)
// 		{
// 				c = a+b;
// 				a = b;
// 				b = c;
// 				if ( c%2 === 0)
// 					sum = sum + c;
// 		}
// 		console.log(sum);
// }
