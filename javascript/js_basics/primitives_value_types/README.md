# Primitives / Value Types

## Section Contains:

*Eight Parts*:

1. The Decscription of *Primitives*/*Value Types* and why they are used.
2. Description and Examples of *Strings*
3. Description and Examples of *Numbers*
4. Description and Examples of *Booleans*
5. Description and Examples of *Undefined*
6. Description and Examples of *Null*
7. Description and Examples of *BigInt*
8. Description and Examples of *Symbols*

#### This file includes:

* Link to the *Primitives* / *Value Types* file: [Primitives / Value Types](primitives_value_types_code/index.js "Primitives / Value Types file")
* Screenshots of each *Value Type* application and the output

##### *HTML* code that was used for these application

![HTML code IMG 1](img/value_types_img_2.PNG "HTML code IMG 1")

# Primitives / Value Types Description:

* *Primitives*/*Value Types*: are basic data types that represent simple pieces of information
* These *Value Types* are:
> * String
> * Number
> * Boolean
> * Undefined
> * Null
> * BigInt
> * Symbol

# String

* *String*: This data type represents a sequence of characters. Strings are enclosed in single or double quotes. For example, “Hello World!” is a string.

### Example

![String IMG 1](img/strings_img_1.PNG "String IMG 1")

### Output

##### *String* application running in the Browser Console

![String IMG 2](img/strings_img_2.PNG "String IMG 2")

##### *String* application running in Command Prompt

![String IMG 3](img/strings_img_3.PNG "String IMG 3")


# Number 

* *Number*: This data type represents a numerical value. It can be an integer or a floating-point number. For example, 5, 10.2, -3.5 are all numbers. Some numbers may not be represented accurately. This is due to rounding errors, which can be avoided by using "toFixed()" method to round the total.

### Example

![Number IMG 1](img/numbers_img_1.PNG "Number IMG 1")

### Output

##### *Number* application running in the Browser Console

![Number IMG 2](img/numbers_img_2.PNG "Number IMG 2")

##### *Number* application running in the Command Prompt

![Number IMG 3](img/numbers_img_3.PNG "Number IMG 3")



# Boolean

* *Boolean*: This data type represents a logical value, either true or false. (T/F can not be used as variables because they are reserved keywords)

### Example

![Boolean IMG 1](img/boolean_img_1.PNG "Boolean IMG 1")

### Output

##### *Boolean* application running in the Browser Console

![Boolean IMG 2](img/boolean_img_2.PNG "Boolean IMG 2")

##### *Boolean* application running in the Command Prompt

![Boolean IMG 3](img/boolean_img_3.PNG "Boolean IMG 3")



# Undefined

* *Undefined*: This data type represents a value that is not defined.

### Example

![Undefined IMG 1](img/undefined_img_1.PNG "Undefined IMG 1")

### Output

##### *Undefined* application running in the Browser Console

![Undefined IMG 2](img/undefined_img_2.PNG "Undefined IMG 2")

##### *Undefined* application running in the Command Prompt 

![Undefined IMG 3](img/undefined_img_3.PNG "Undefined IMG 3")



# Null

* *Null*: This data type represents a null or empty value.

### Example

![Null IMG 1](img/null_img_1.PNG "Null IMG 1")

### Output

##### *Null* application running in the Browser Console

![Null IMG 2](img/null_img_2.PNG "Null IMG 2")

##### *Null* application running in the Command Prompt

![Null IMG 3](img/null_img_3.PNG "Null IMG 3")



# BigInt

* *BigInt*: This data type represents integers that are larger than 2⁵³-1 or smaller than -(2⁵³-1). 

### Example

![BigInt IMG 1](img/bigint_img_1.PNG "BigInt IMG 1")

### Output

##### *BigInt* application running in the Browser Console

![BigInt IMG 2](img/bigint_img_2.PNG "BigInt IMG 2")

##### *BigInt* application running in the Command Prompt

![BigInt IMG 3](img/bigint_img_3.PNG "BigInt IMG 3")



# Symbol

* *Symbol*: This data type represents a unique value that cannot be duplicated. Often used as keys in objects to avoid naming issues

### Example

* A function was used to demonstrate a useful way to use symbols.

![Symbol IMG 1](img/symbols_img_1.PNG "Symbol IMG 1")

### Output

* Output is only displayed in Browser Console due to node not allowing the use of "prompt". There is a way to have user inputs in node, it just uses a different method. For this application I used "prompt".

##### *Symbol* application prompting the user for a user ID

![Symbol IMG 2](img/symbols_img_2.PNG "Symbol IMG 2")

##### *Symbol* application recieving user input as "12345" prompts the system to check for any users with that ID number.

![Symbol IMG 3](img/symbols_img_3.PNG "Symbol IMG 3")

##### *Symbol* application returns with a user because that specific ID number is in the sytem.

![Symbol IMG 4](img/symbols_img_4.PNG "Symbol IMG 4")

##### *Symbol* application recieving user input as "123456" prompts the system to check for any users with that ID number.

![Symbol IMG 3](img/symbols_img_5.PNG "Symbol IMG 5")

##### *Symbol* application returns with "ID not found in system!" because ID is not in the system.

![Symbol IMG 6](img/symbols_img_6.PNG "Symbol IMG 6")

