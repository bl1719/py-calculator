#main functions

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

def main():
    print('Type 1 2 3 or 4 corresponding to your operator:')
    choice = input("Type in your choice")
    num1 = float(input("Type in your first number"))
    num2 = float(input("Type in your second number"))

    if choice == '1':
        print('Your answer is', add(num1, num2))
    elif choice == '2':
        print('Your answer is', subtract(num1, num2))
    elif choice == '3':
        print('Your answer is', multiply(num1, num2))
    elif choice == '4':
        print('Your answer is', divide(num1, num2))
    else:
        print('Invalid Input')

main()
    
