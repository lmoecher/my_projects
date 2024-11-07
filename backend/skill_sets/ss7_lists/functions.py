def get_requirements(): 
    print("Developer: Logan Moecher")
    print("Python Lists")
    print("\nProgram Requirments:\n"
        + "1. Lists (Python data structure): mutable, ordered sequence of elements.\n"
        + "2. Lists are mutable/changeable--that is, can insert, update, delete.\n"
        + '3. Create list - using square brackets[list]: my_list = ["cherries", "apples", "bananas", "oranges"].\n'
        + "4. Create a program that mirrors the following IPO (input/process/output)format.\n"
        + "Note: user enter number of request list elements, dynamically rendered below(that is, number of elements can change each run).\n")

# IPO: Input > Process > Output

def user_input():
    # initialize variables and list
    num = 0

    # Input: get user data
    print("Input: ")
    num = int(input("Enter number of list elements: "))
    return num

print ()    #print blank line

def using_lists(num):
    # Process:
    my_list = []    #create an empty list

    #range(stop)
    # stop: Number of integers (whole numbers) to generate,
    # starting from zero; e.g., range(3) == [0, 1, 2]
    for i in range(num):    # run loop num times (0 to num)
        # prompt user for list element
        my_element = input('Please enter list element ' + str(i + 1) + ": ")
        my_list.append(my_element)      # append each element to end of list

    # Output:
    print("\nOutput: ")
    print("Print my_list: ")
    print(my_list)

    elem = input("\nPlease enter list element: ")
    pos = int(input("Please enter list 'index' position (note: must convert to int): "))

    print("\nInsert element into specific position in my_list")
    my_list.insert(pos, elem)   #Note: pos 1 insert item into 2nd element
    print(my_list)

    print("\nCount number of elements in list: ")
    # also works for strings, tuples, dict opjects
    print(len(my_list))

    print("\nSort elements in list alphabetically: ")
    my_list.sort()   # sort alphabetically
    print(my_list)

    print("\nReverse list: ")
    my_list.reverse()   # reverse list
    print(my_list)

    print("\nRemove last list element: ")
    my_list.pop()   # delete last element (LIFO)
    print(my_list)

    print("\nDelete second element from the list by 'index' (note: 1 = 2nd element): ")
    # pops element at index specified
    # my_list.pop
    del my_list[1]   
    print(my_list)

    print("\nDelete elements from list by 'value' (cherries): ")
    my_list.remove("cherries")
    print(my_list)

    print("\nDelete elements from list: ")
    my_list.clear()     # delete all items from the list
    print(my_list)