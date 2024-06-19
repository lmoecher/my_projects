// Functions are a set of statements that perform a task or calculates and returns a value
// The Parameter is at the time of declaration and the Argument is the actual value that supplies that parameter
// (name) inside the parentheses is referred a parameter to the greet function
// ('Logan') is referred to as an argument to the greet function
// Functions can have multiple parameters, add more by adding a ','
// Realworld apps have thousands of functions runnning together to provide the functionality of that application

function greet(name, lastName) {     
    console.log('Hello ' + name + ' ' + lastName); // The + concatenates the two strings
} // Inside the curly brackets is known as the body of the function

greet('Logan'); // This statement is calling the function
greet('Mokes'); // this causes them to show up on separate lines and be value as undefined

// A ; is not needed behind the curly bracket because is is not being declared  like a variable.


// Cleaner Version of the same Function

function greet(name, lastName) {
    console.log('Hello ' + name + ' ' + lastName);
}

greet('Logan', 'Moecher');

// Calculates a value
function square(number) {
    return number * number;
}
 
console.log(square(2));