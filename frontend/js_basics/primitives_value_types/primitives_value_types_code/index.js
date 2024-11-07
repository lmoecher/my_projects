// Primitives/ Value Types are basic data types that represent simple pieces of information 

// String: This data type represents a sequence of characters.
// Strings are enclosed in single or double quotes. For example, “Hello, world!” is a string.

// Number: This data type represents a numerical value. It can be an integer or a floating-point number. 
// For example, 5, 10.2, -3.5 are all numbers. Some numbers may not be represented accurately.
// This is due to rounding errors, which can be avoided by using "toFixed()" methos to round the total.

// Boolean: This data type represents a logical value, either true or false.
// (T/F can not be used as variables because they are reserved keywords)

// Undefined: This data type represents a value that is not defined.

// Null: This data type represents a null or empty value.

// BigInt: This data type represents integers that are larger than 2⁵³-1 or smaller than -(2⁵³-1). 

// Symbol: This data type represents a unique value that cannot be duplicated.
// Often used as keys in objects to avoid naming issues. 

// String 
{
    let firstName = 'Logan'; // String literal
    let lastName = 'Moecher';
    let myName = firstName + " " +  lastName;
    console.log(myName); // Output: Logan Moecher
}

// Number
{
    let num1 = 10; // Number literal
    let num2 = 16;
    let num3 = num1 + num2;
    console.log(num3); // Output: 26
}

// Boolean
{
    let age = 18;
        if (age >= 18) {
            console.log("You're an adult.");
        } else {
            console.log("You're a minor.");
        }
}

// Undefined
{
    let myVariable;
    console.log(myVariable);
}

// Null
{
    let selectedColor = null; 
} 

// BigInt
{
    let num1 = 3.14159265359; 
}

// Symbol
{
    const person = {
        firstName: "Logan",
        lastName: "Moecher",
        age: 26,
        height: 6 + " " + "ft" + " " + 3 + " " + "inches",
        eyeColor: "Blue",
        hairColor: "Brown",
    };

    let id = Symbol('id');
    person[id] = 12345;

    function getPersonById(givenId){
        if (person[id] === givenId){
            return `Id: ${person[id]} is shown below\n
            First Name: ${person.firstName}\n
            Last Name: ${person.lastName}\n
            Age: ${person.age}\n
            Height: ${person.height}\n
            Eye Color: ${person.eyeColor}\n
            Hair Color: ${person.hairColor}`; 
        } else {
            return `ID not in the System!`;
        }
    }
    {
    let searchId = prompt("To search a user, please input their ID number.");
    searchId = Number(searchId);
    const result = getPersonById(searchId);
    console.log(result); // Output: Will show persons info if they are in the system
    }
}
