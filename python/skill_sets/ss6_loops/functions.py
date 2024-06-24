def get_requirements():
   
    print("Developer: Isaiah Newton")
    print("Python Loops")
    print("\nProgram Requirements:\n"
    +"1. Print while loop.\n"
    +"2. Print for loops using range() function, and implicit and explicit lists.\n"
    +"3. Use break and continue statements.\n")
 
def whiloop():
    i = 1
    print('1. While loop')
    while i <= 3:
        print(i)
        i+=1

def forloop():
    print('2. for loop: using range() function with 1 arg')
    for i in range(4):
        print(i)

def forloop2():
    print('3. for loop: using range() function with 2 args')
    for i in range(1,4):
        print(i)

def forloop3():
    print('4. for loop: using range() function with 3 args(interval 2):')
    for i in range(1,4,2):
        print(i)

def forloop4():
    print('5. for loop with using range() function with 3 args(negative interval)')
    for i in range(3,0,-2):
        print(i)

def forloop5():
    print('6. for loop using (implicit) list')
    l = [1, 2, 3]
    for item in l:
        print(item)

def forloopEx(ls):
    print('7. for loop iterating through explicit list')
    for item in ls:
        print(item)

def forloopbreak(ls):
    print('8. for loop using break')
    for item in ls:
        if item == 'Alabama':
            break
        else: print(item)


def forloopcont(ls):
    print('9. for loop using continue statement')
    for item in ls:
        if item == 'Alabama':
            continue
        else:
            print(item)

def listlen(ls):
    print('10. print list length')
    print(len(ls))

def main():
    lics = ['Michigan', 'Alabama', 'Florida']
    get_requirements()
    print()  
    whiloop()
    print()
    forloop()
    print()
    forloop2()
    print()
    forloop3()
    print()
    forloop4()
    print()
    forloop5()
    print()
    forloopEx(lics)
    print()
    forloopbreak(lics)
    print()
    forloopcont(lics)
    print()
    listlen(lics)

main()