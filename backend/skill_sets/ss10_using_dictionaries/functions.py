

def get_requirements(): 
    print("Developer: Logan Moecher")
    print("Python Dictionaries!")
    print("\nProgram Requirments:\n"
        + "1. Dictionaries (Python data structure): unordered key: value pairs.\n"
        + "2. Dictionaries: an associative array (also known hashes).\n"
        + "3. Any key in a dictionary is associated (or mapped) to a value (i.e., any Python data type).\n"
        + "4. Keys: must be of immutable type (string, number or tuple with immutable elements) and must be unique.\n"
        + "5. Values: can be any data type and can repeat.\n"
        + "6. Create a program that mirrors the following IPO (Input/Process/Output) format.\n"
        + "\tCreate empty dictionary, using curly braces {}: my_dictionary = {}.\n"
        + "\tUse the following keys: fname, lname, degree, major, gpa\n"
        + "Note: Dictionaries have key-value pairs instead of single values; this differentiates a dictionary from a set.\n")

def using_dictionaries():
    v_fname = ""
    v_lname = ""
    v_degree = ""
    v_major = ""
    v_gpa = 0.0
    my_dictionary = {} # create empty dictionary 

    #IPO (Input/Process/Output)
    # get user data
    print("Input: ")   
    # Note: v_indicates variable, differentiates from key name 
    v_fname = input("First Name: ")
    v_lname = input("Last Name: ")
    v_degree = input("Degree: ")
    v_najor = input("Major (IT or ICT): ")
    v_gpa = float(input("GPA: "))

    print()

    # Process (note: key names)
    my_dictionary['fname'] = v_fname
    my_dictionary['lname'] = v_lname
    my_dictionary['degree'] = v_degree
    my_dictionary['major'] = v_major
    my_dictionary['gpa'] = v_gpa

    # Output: 
    print("\nOutput: ")
    print("Print my_dictionary")
    print(my_dictionary)

    print("\nReturn view of dictionary's (key, value) pair, built-in-function:")
    print(my_dictionary.items())

    print("\nReturn view object of all keys, built-in-function:")
    print(my_dictionary.keys())

    print("\nReturn view object of all values in dictionary, built-in-function:")
    print(my_dictionary.values())

    print("\nPrint only first and last names, using keys: ")
    print(my_dictionary['fname'], my_dictionary['lname'])

    print("\nPrint only first and last names, using get() function: ")
    print(my_dictionary.get("fname"), my_dictionary.get("lname"))

    print("\nCount number of items (key:value pairs) in dictionary: ")
    # also works for strings, tuples, list elements
    print(len(my_dictionary))

    print("\nRemove last dictionary item (popitem): ")
    my_dictionary.popitem() # delete last item
    print(my_dictionary)

    print("\nDelete major from dictionary, using key: ")
    # pop item using specified key
    my_dictionary.pop("major")
    # or...
    # del my_dictionary["major"]
    print(my_dictionary)

    print("Return object type: ")
    print(type(my_dictionary))

    print("\nDelete all item from list: ")
    my_dictionary.clear()   # delete all items
    print(my_dictionary)    # Note: here, my_dictionary still exists
    # different from...

    # delete entire dictionary object (no longer exists)
    del my_dictionary
    # print(my_dictionary) # UnboundLocalError: local variable 'my_dictionary'
