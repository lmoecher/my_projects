def get_requirements(): 
    print("Developer: Logan Moecher")
    print("Python Tuples")
    print("\nProgram Requirments:\n"
        + "1. Tuples (Python data structure): *immutable* (cannot be changed!), ordered sequence of elements.\n"
        + "2. Tuples are immutable/unchangable--that is, cannot insert update, delete. \nNote: can reassign or delete an *entire* tuple--but, *not* individualnitems or slices.\n"
        + '3. Create tuple using parentheses (tuple): my_tuple1 = ("cherries", "apples", "bananas", "oranges")\n'
        + '4. Create tuples (packing), that is, *without* using parentheses (aka tuple \ "packing\'): my_tuple2 = 1, 2, "three", "four"\n'
        + '5. Python tuple (unpacking),that is, assign values from tuple to sequence of variables: fruit1, fruit2, fruit3, fruit4 = my_tuple1.\n'
        + "6. Create a program that mirrors the following IPO (input/process/output) format.\n")

def using_tuples():
    #   Input:
    print("\nInput: Hard coded--no user input.")

    #   Initialize variables and tuples
    my_tuple1 = ("cherries", "apples", "bananas", "oranges")    #create tuple

    # Note: comma *not* parentheses define tuples
    # create tuples using parentheses
    my_tuple2 = 1, 2, "three", "four"

    # Output
    print("\nOutput: ")
    print("Print my_tuple1: ")
    print(my_tuple1)

    print()

    print("Print my_tuple2: ")
    print(my_tuple2)

    print()
    # tuple unpacking
    fruit1, fruit2, fruit3, fruit4 = my_tuple1
    print("Print my_tuple1 unpacking:")
    print(fruit1, fruit2, fruit3, fruit4)

    print()
    print("Print third element in my_tuple2: ")
    print(my_tuple2[2])

    #   Note: indexing begins at 0. That is, 1 begins on second element.
    #   And, 3 indicates to end at the fourth element, "but" not include it.
    #   Colon used in Python for slicing objects.

    print()
    print("Print\"slice\" of my_tuple1 (second and third elements):")
    print(my_tuple1[1:3])

    print()
    print("Reassign my_tuple2 using parentheses.")
    my_tuple2 = (1, 2, 3,4)
    print("Print my_tuple2: ")
    print(my_tuple2)

    print()
    print("Reassign my_tuple2 using \"packing\" method (no parentheses).")
    my_tuple2 = 5, 6, 7, 8

    print("Print my_tuple2: ")
    print(my_tuple2)

    print()
    print("Print number of elements in my_tuple1: " + str(len(my_tuple1)))

    print()
    print("Print type of my_tuple1: " + str(type(my_tuple1)))

    # print(type(my_tuple1)) # or, can do this

    print()
    print("Delete my_tuple1: \nNote: will generate error, if trying to print after, as it no longer exsits.")
    del my_tuple1
    # print(my_tuple1) # Note: will generate error, as it no longer exsits

