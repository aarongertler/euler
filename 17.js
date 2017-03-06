// If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
// then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

// If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
// how many letters would be used?


// NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
// contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
// The use of "and" when writing out numbers is in compliance with British usage.

var letterCount = function(n) {
	switch(n) {
		case 1: return 3;	break;
		case 2: return 3;	break;
		case 3: return 5;	break;
		case 4: return 4;	break;
		case 5: return 4;	break;
		case 6: return 3;	break;
		case 7: return 5;	break;
		case 8: return 5; break;
		case 9: return 4; break;
		case 10: return 3; break;
		case 11: return 6; break;
		case 12: return 6; break;
		case 13: return 8; break;
		case 14: return 8; break;
		case 15: return 7; break;
		case 16: return 7; break;
		case 17: return 9; break;
		case 18: return 8; break;
		case 19: return 8; break;
		case 20: return 6; break;
		case 30: return 6; break;
		case 40: return 5; break;
		case 50: return 5; break;
		case 60: return 5; break;
		case 70: return 7; break;
		case 80: return 6; break;
		case 90: return 6; break;
		default: return 0;
	}
} 

console.log(letterCount(12));

var numberOfLetters = function(n) { // Find the number of letters in a given word.
	var numSum = 0;
	if(n % 100 === 0) {
		return letterCount(n / 100) + 7;
	}
	// if(n.length === 3) {
	// 	numSum += 10;     // Add "hundred and" to other three-digit numbers
	// }
	if(letterCount(n) != 0) {
		return letterCount(n);    // If we have this number in our "database", just return it
	}
	else if(n.toString().length === 2) {
		numSum += (numberOfLetters(n - (n % 10)) + numberOfLetters(n % 10));
	}
	else {
		numSum += (numberOfLetters(n - (n % 100)) + numberOfLetters(n % 100) + 3);
	}
	return numSum;
}

console.log(numberOfLetters(2));
console.log(numberOfLetters(42));
console.log(numberOfLetters(300));
console.log(numberOfLetters(342));

var total = 11;  // Pre-adding the letters from "one thousand" to our total

for(i = 1; i < 1000; i++) {
	total += numberOfLetters(i);
}

console.log("The total is: " + total);