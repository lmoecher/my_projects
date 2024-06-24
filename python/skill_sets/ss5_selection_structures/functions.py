def get_requirements():
    print("Python Selection Structures")
    print("\nProgram Requirements:\n"
        +"1. Use Python selection structure.\n"
        +"2. Promt user for two numbers, and a suitable operator\n"
        +"3. Test for correct numeric operator.\n"
        +"4. Replicate display below."
        +"")
   
   
def python_calculator(a, b, c):
    if c == '+':
        print(a+b)
    elif c == '-':
        print(a-b)
    elif c == '/':
        print(a/b)
    elif c == '*':
        print(a*b)
    elif c == '//':
        print(a//b)
    elif c == '%':
        print(a%b)
    elif c == '**':
        print(pow(a,b))
    else:
        print('Incorrect operator!')

def main():
    get_requirements()
    print()
    print("Python Calculator")
    num1 = float(input('Enter Num1: '))
    num2 = float(input('Enter Num2: '))
    print()
    print("Suitable Operators: +,-,*,/,//(integer division),%(modulo operator),**(power)")
    op = input('Enter Operator: ')
    python_calculator(num1, num2, op)

main()