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
	c = [];    					// Array that stores the answer
	for(var i = 0; i < b.length; i++) {     // Move along the bottom "row" of digits
		for(j = 0; j < a.length; j++) {
			var placeVal = (a.length-j-1)+(b.length-i-1);  // For 3-digit number * 2-digit number, placeVal starts out as "3", for an index of 3 = thousands place
			if(c[placeVal] === undefined) {
				c[placeVal] = 0;
			}
			c[placeVal] += b[i]*a[j];  // Each place is added at least twice -- for 170*15, we add 10*70 and 100*5 to the "hundreds" place
		}
	}
	return c.reverse();    // aTimesB("150","17") would return a 1 in the thousands place, 12 in the hundreds place, 35 in the tens place, 0 in the ones place
}

var convertArrayToString = function(a) {     // Convert an array full of place values to a long number as a string
	for(var i = 0; i < a.length; i++) {
		if(a[i] >= 10) {      // Needed >= 10, not > 10 --> that took some debugging!
			if(a[i+1] === undefined) {     // Make sure we don't carry over a number into a non-existent spot
				a[i+1] = 0;
			}
			a[i+1] += ((a[i] - (a[i] % 10)) / 10); // tens digit
			a[i] = a[i] % 10; // ones digit
		}
	}
	return a.join("").toString();
}

console.log(aTimesB("150","17"))




var factorialDigits = function(n) {  // Enter 100 to get 100! as a string
	value = 1;
	for(var i = 2; i < n + 1; i++) {   // Remember to re-declare loop variables!
		value = convertArrayToString(aTimesB(value.toString(),i.toString()));
	}
	return value;
}

// console.log(typeof factorialDigits(10)) 

var digitSum = function(n) {   // You'll be doing a lot of this with Project Euler, put this somewhere to reuse?
	var sum = n.reduce(function(a,b){return a+b});
	return sum
}

console.log(digitSum(digitize(factorialDigits("100"))))
// console.log(digitSum(digitize("93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000")))


// Ways to make this faster/better: Borrow string-multiplication functions from existing JS functions, reduce the 
// number of times you convert values from arrays to strings and back again, do the early factorials as math and start with 20! instead of 1


// Note: The inability of JS to work with large numbers has become a problem; switch to Python?