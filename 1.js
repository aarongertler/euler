var last = 1000

var sum = 0

var threeFive = function(last) {
	for(var number = 0; number < last; number++) {
		if(number % 3 === 0 || number % 5 === 0) {
			sum += number;
		}
	}
}

threeFive(last)

console.log(sum)



// Simpler solution, not as versatile

// var sum = 0;
// for (i = 0; i < 1000; i++){
//     if (i % 3 === 0||i % 5 ===0){
//         sum += i;
//     }
// }
// console.log(sum)