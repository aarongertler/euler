// The Fibonacci sequence is defined by the recurrence relation:

// Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
// Hence the first 12 terms will be:

// F1 = 1
// F2 = 1
// F3 = 2
// F4 = 3
// F5 = 5
// F6 = 8
// F7 = 13
// F8 = 21
// F9 = 34
// F10 = 55
// F11 = 89
// F12 = 144
// The 12th term, F12, is the first term to contain three digits.

// What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

// Just looking at the first four digits should be very close to accurate

var firstFew = function(n,d) {
	n = n.toString();
	n = n.substring(0,d);
	n = parseInt(n);
	return n;
}

var cutoff = 15 // only take the first fifteen digits (raise if needed)

var digits = cutoff;

var trueFib = function(n) {
	var steps=0
	var a = 0;
	var b = 1;
	var c = 1;
	while(steps < n) {
		a = b
		b = c
		c = a + b;
		steps++
		console.log(c);
	}
}

var fakeFib = function(n) {    // We need the estimator, node only counts up to 308 digits
	var steps = 2;
	var a = 0;
	var b = 1;
	var c = 1;
	var d = cutoff;
	while(digits < n) {
		a = b
		b = c
		c = a + b;
		if(c.toString().length > d) {
			digits++
			a = firstFew(a,d-1)
			b = firstFew(b,d-1)
			c = firstFew(c,d)
		}
		steps++
		console.log(c);
	}
	return steps;
}

// console.log(trueFib(77));    
// console.log(fakeFib(17));

// Other idea: Just take exponents of the Golden Ratio?

// I mean, we could also just make an "aPlusB" function that mimicked addition using arrays, but I've
// done that sort of thing already. I'll use this as estimator practice.


// Never mind. We're getting very close to the answer with the estimators (probably within 5), 
// but I don't like the feeling of just guessing. Let's do this the right way. (Sigh.)

var aPlusB = function(a,b) {   // pass in two arrays that we will add
	var a = a.reverse()    // adding from right to left for simplicty
	var b = b.reverse()
	var c = [];     // this array holds the result
	for(var i = 0; i < b.length; i++) {   // Using b as the "reference point" for now
		if(c[i] === undefined) {
			c[i] = 0;
		}
		if(a[i] === undefined) {
			a[i] = 0;
		}

		var sum = b[i] + a[i];
		c[i] += (sum % 10);
		c[i] = c[i] % 10;

		if(sum >= 10) {
			c[i+1] = 1;
		}
	}
	return c.reverse();
}


var finalFib = function(n) {
	var steps = 2;
	var a = [0];
	var b = [1];
	var c = [1];
	while(c.length < n) {
		a = b.reverse()    // We were getting double-reversed somewhere, this fix is a hack
		b = c
		c = aPlusB(a,b);
		console.log(c);
		steps++
	}
	return steps;
}

console.log(finalFib(20));
// console.log(aPlusB([9,6,1,1],[9,9,6,8]))


// This solution is highly accurate for as many digits as I can reasonably count, but gives a
// final answer for 1000 digits that is not correct. Not sure why.

// Turns out that my estimator actually does give the correct answer, when I account for the first two
// "steps" taken by having c already equal to 2 at the beginning

