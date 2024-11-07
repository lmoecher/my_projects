
import random

def get_requirements(): 
    print("Developer: Logan Moecher")
    print("Psuedo-Random Number Generator")
    print("\nProgram Requirments:\n"
        + "1. Get user beginnning and ending integer values, and store in two variables.\n"
        + "2. Display 10 psuedo-random numbers between, and including, above values.\n"
        + "3. Must use integer data types.\n"
        + "4. Example 1: Uusing range() and randint() functions.\n"
        + "5. Example 2: Using a list with range() and shuffle functions.\n")

def random_numbers():
    # initialize variables
    # get user data
    print("Input: ")
    start = int(input("Enter beginning value: "))
    end = int(input("Enter ending value: "))

    # Process and Output
    # Display 10 random numbers between start and end, inclusive
    # print(): http://www.programiz.com/python-programming/methods/built-in/print

    # range() function returns a sequence of numbers
    # range(start, stop, step) - must be integer numbers
    # Note: start(optimal, default 0), stop (required, noninclusive), step (optional, default 1)

    my_sequence = range(6)
    for item in my_sequence:
        print(item)

    print("\nOuput: ")
    print("Example 1: Using range() and randint() functions: ")
    # Here, range just used to print 10 numbers
    # However, randint(start, end) used to print range of integers (inclusive)
    for item in range(10):
        print(random.randint(start, end), sep=", ", end =" ")

    print()

    print("\nExample 2: Using a list, with range() and shuffle() functions: ")
    #
    #
    #
    my_list = list(range(start, end + 1))
    random.shuffle(my_list) # recognize list item
    for item in my_list:
        print(item, sep=", ", end=" ")

    print()