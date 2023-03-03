const n = parseInt(prompt('Enter the number of terms: ')); 

let t1 = 0, t2 = 1; 
let nextTerm; 

console.log('Fibonacci Series: '); 

for(let i = 1; i <= n; i++)
  {
    console.log(t1)' 
    nextTerm = t1 + t2; 
    t1 = t2; 
    t2 = nextTerm; 
  }
