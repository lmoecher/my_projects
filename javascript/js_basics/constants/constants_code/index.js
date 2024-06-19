// Constant is a keyword that allows users to assign a name to a value
// A value of a const cannot change
// This is why it shows up as undefined when ran through the second version 

// Version one without const 
{
let interestRate = 0.3;
 interestRate = 1;
 console.log(interestRate);
} 

// Version2 when const is used and declared as 3.0 through interestRate 
// Thus showing up as undefined because its value cannot change
{
const interestRate = 0.3;
interestRate = 1;
console.log(interestRate);
}