// You are given the following information, but you may prefer to do some research for yourself.

// 1 Jan 1900 was a Monday.
// Thirty days has September,
// April, June and November.
// All the rest have thirty-one,
// Saving February alone,
// Which has twenty-eight, rain or shine.
// And on leap years, twenty-nine.
// A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

// How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

function contains(a, obj) {
    for (var i = 0; i < a.length; i++) {
        if (a[i] === obj) {
            return true;
        }
    }
    return false;
}

var calendar = function(n,d,m,y) {   // return the day, month, and year n days from your starting d,m,y
	var sundayCount = 0;
	var thirtyMonths = [4,6,9,11]
	var thirtyOneMonths = [1,3,5,7,8,10,12]
	for(i = 1; i < n + 1; i++) {
		d++  // Start by adding a day to the calendar
		if(d === 29 && m === 2 && (y % 4 != 0 || ((y % 100 === 0) && (y % 400 != 0)))) {   // February 28th, no leap year
			d = 1;
			m++;
		}
		if(d === 30 && m === 2 && y % 4 === 0 && (y % 100 != 0 || y % 400 === 0)) {   // February 29th, leap year
			d = 1;
			m++;
		}
		if(contains(thirtyMonths, m) && d === 31) {
			d = 1;
			m++;
		}
		if(contains(thirtyOneMonths, m) && d === 32) {
			d = 1;
			m++;
		}
		if(m === 13) {  // Start over in a new year
			m = 1;
			y++;
		}
		// console.log(d + "," + m + "," + y);
		if((i % 7 === 0) && (d === 1)) {
			sundayCount++;
		}
		if((i % 7 === 0) && (d === 1)) {
			console.log([d,m,y,sundayCount]);
		}
	}
	// return[d,m,y,sundayCount];
}

console.log(calendar(36890,0,1,1901))   // Start from 1/1/1901, not 1900

// Easier way to do this: Just use date/time API to check each day. Sort of like cheating, but also very basic programming...