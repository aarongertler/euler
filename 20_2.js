// A big-number-based solution to 20, from http://stackoverflow.com/questions/3959211/fast-factorial-function-in-javascript

var BigNumber = require('bignumber.js');

var f = [new BigNumber("1"), new BigNumber("1")];
    var i = 2;
    function factorial(n)
    {
      if (typeof f[n] != 'undefined')
        return f[n];
      var result = f[i-1];
      for (; i <= n; i++)
          f[i] = result = result.multiply(i.toString()); // the multiply function seems to require a library I don't have
      return result;
    }
    var cache = 100;
    console.log(factorial(cache));