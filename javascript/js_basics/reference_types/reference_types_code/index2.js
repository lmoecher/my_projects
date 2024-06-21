// Array
{
    let selectedColors = ['red', 'blue']; // red: 0, blue: 1
    selectedColors[2] = 1;
    console.log(selectedColors.length); // .length returns the number of items or elements in an array
}

//Function
{
    // (name) inside the parentheses is referred a parameter to the greet function
    // ('Logan') is referred to as an argument to the greet function
    function greet(name, lastName) {     
        console.log('Hello ' + name + ' ' + lastName); // The + concatenates the two strings
} // Inside the curly brackets is known as the body of the function

    greet('Logan'); // This statement is calling the function
    greet('Mokes'); // This causes them to show up on separate lines and be value as undefined
} // A ";" is not needed behind the curly bracket because it is not being declared  like a variable

// Cleaner Version of the same Function
{
    function greet(name, lastName) {
        console.log('Hello ' + name + ' ' + lastName);
}
    greet('Logan', 'Moecher');
}

// Function that calculates a value
{
    function square(number) {
        return number * number;
}
    console.log(square(2));
}

// Objects are the properties of the variables

// Dot Notation 
{
    let person = {
        name: 'Logan', // Objects
        age: 26
    };  // "{}" Curly Brackets are known as an Object Literals

    person.name = 'Mr. Moecher'
    console.log(person.name);
}


//Bracket Notation
{
    let person = {
        name: 'Logan', // Objects
        age: 26
    }; // "{}" Curly Brackets are known as an Object Literals

    let selection = 'name'
    person[selection] = 'Mr. Moecher';
    console.log(person.name);
}