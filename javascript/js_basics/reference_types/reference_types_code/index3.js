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