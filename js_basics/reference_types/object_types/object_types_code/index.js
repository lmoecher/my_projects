// Objects are the properties of the variables


let person = {
    name: 'Logan',
    age: 26
};  // "{}" Curly Brackets are known as an Object Literal

// 2 ways of changes the name of person and accessing the properties
// Dot & Bracket Notation: Stick to Dot Notation as it is not as consice as Bracket Notation needs to be

// Dot Notation 
person.name = 'Mr. Moecher'

//Bracket Notation
let selection = 'name'
person[selection] = 'Mokes';

console.log(person.name);