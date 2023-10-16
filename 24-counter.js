i=-1
var createCounter = function(n) {
    console.log(n)
    return function(n) {
      
        i+=1
        console.log(n)
        return n+i
    };
};

a=createCounter(10)
console.log(a)