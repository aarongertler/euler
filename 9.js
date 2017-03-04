// A Pythagorean triplet is a set of three natural numbers, a < b < c, for which:

// a^2 + b^2 = c^2
// For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
// Find the product abc.


var isTriplet = function(a,b,c) {
	if(Math.pow(a,2) + Math.pow(b,2) === Math.pow(c,2)){ return true; }
	else { return false; }
}

// console.log(isTriplet(3,4,5))
// console.log(isTriplet(3,4,6))
// console.log(isTriplet(210,280,350))


for(a = 3; a < 334; a++) {
	for(b = a; b < 500; b++) {     // assume b > a
		for(c = b + 4; c < 1000; c++) {  // c > b + 3 (as 3,4,5 is the smallest triple); also, c < 500, since (500, 499, 1) doesn't work 
			if(isTriplet(a,b,c)) {
				console.log(a + "," + b + "," + c);
				if(a+b+c === 1000) { 
					console.log(a + "," + b + "," + c + " is the answer!")
					return true; 
				}
			}
		}
	}
}


// Making this faster:
// For small triangle perimeters, finding better bounds for the numbers will help

// For bigger triangles (e.g. finding a triplet that sums to ten million):
// It helps to know that, for any m and n where m > n > 0, the greatest common denominator is 1, and m or n is even, a triplet can be formed thus:
// a = m^2 - n^2    b = 2mn     c = m^2 + n^2
// Those are primitive triplets, with a GCD of 1 (e.g. 3,4,5). We can turn them into bigger, proportional triplets (e.g. 6,8,10) if we multiply by an integer (d)
// So all triplet sums take the form   a + b + c = d * (2)(m)(m+n)
// More math:    1000 = d*2(m)(m+n)    500 = d(m)(m+n)  where m and n have no common denominators, and one of them is even
// This reduces the search space considerably. So we can loop over a range of m (where m < sqrt(500)-1), then do a bit more algebra...
// ...anyway, it's all in the PDF. This one's really interesting, but I won't give the full answer away here.