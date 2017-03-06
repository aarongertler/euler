// Return the sum of the digits of 100!

// var factorialDigits = function(n) {
// 	let memo = n;
// 	for(i = 1; i < memo - 1; i++) {
// 		n = n*(memo-i);
// 		console.log(n);
// 		while(n % 10 === 0) {
// 			n = n / 10;
// 			console.log("n over 10 = " + n);
// 		}
// 	}
// 	return n;
// }

// console.log(factorialDigits(25))

// Yeah, looks like trying to trim the factorial of excess zeros just isn't going to cut it
// Time for generalized very-large-number multiplication functions!

var digitize = function(n) {     // Turn n into an array of digits of length n ("100" becomes [1,0,0])
	let array = [];
	for(var i = 0; i < n.length; i++) {
		array[i] = parseInt(n.charAt(i));
	}
	return array;
}

// console.log(digitize(72343))

var aTimesB = function(a,b) {    // Take a string and "multiply" it by another string, but keep all digits in an array
	a
	b
	c = [];    					// Array that stores the answer
	for(var i = 0; i < b.length; i++) {     // Move along the bottom "row" of digits
		for(j = 0; j < a.length; j++) {
			var placeVal = (a.length-j-1)+(b.length-i-1);
			if(c[placeVal] === undefined) {
				c[placeVal] = 0;
			}
			c[placeVal] += b[i]*a[j];
		}
	}
	return c;
}

var convertArray = function(a) {     // Convert an array full of place values to an array that shows a long number
	for(var i = 0; i < a.length; i++) {
		if(a[i] >= 10) {      // Needed >= 10, not > 10 --> that took some debugging!
			if(a[i+1] === undefined) {     // Make sure we don't carry over a number into a non-existent spot
				a[i+1] = 0;
			}
			a[i+1] += ((a[i] - (a[i] % 10)) / 10);
			a[i] = a[i] % 10;
		}
		// console.log(a[i])
	}
	return a.reverse().join("").toString();
}




var factorialDigits = function(n) {          // n is a string; to get 100!, enter "100"
	value = "1";
	for(var i = 2; i < parseInt(n) + 1; i++) {   // Remember to re-declare loop variables!
		value = convertArray(aTimesB(value,i.toString()));
	}
	return value;
}


var digitSum = function(n) {   // You'll be doing a lot of this with Project Euler, put this somewhere to reuse?
	var sum = n.reduce(function(a,b){return a+b});
	return sum
}

console.log(digitSum(digitize(factorialDigits("100"))))
// console.log(digitSum(digitize("93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000")))


// Make this faster/better: Borrow string-multiplication functions from existing JS functions, reduce the 
// number of times you convert values from arrays to strings and back again


// Note: The inability of JS to work with large numbers has become a problem more often; switch to Python?