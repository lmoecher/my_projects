// Constant is a keyword that allows users to assign a name to a value
// A value of a const cannot change
// This is why it shows up as undefined when ran through the second version 

// Version one without const 
{
 let interestRate = 0.3;
 interestRate = 1;
 console.log(interestRate);
} 

// Version 2 const is used and declared as 0.3 through interestRate 
// It is showing up as undefined because its value cannot change
// Which is what Line 17 is trying to do
{
 const interestRate = 0.3;
 interestRate = 1;
 console.log(interestRate);
}

// Version 3 const is used and declared as 0.3 through interestRate
// Which is why it shows up as 0.3 and can be used by typing "interestRate"
// it runs correctly because interestRate is not trying to be reassigned 
{ 
 const interestRate = 0.3; 
 console.log(interestRate);
}