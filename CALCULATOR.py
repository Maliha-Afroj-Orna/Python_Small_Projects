# Operations
def addition(x, y):
    return x + y


def subtraction(x, y):
    return x-y


def multiplication(x, y):
    return x * y


def division(x, y):
    if y == 0:
        print('Nothing can be divided by zero')
    else:
        return x / y


# main function
def main():
    print('Simple Calculator\n'\
          'Select an Operator:\n'\
          '1. Add\n'\
          '2. Sub\n'\
          '3. Mul\n'\
          '4. Div')


print(main())

# Take input from the user
operator = int(input('Select an Operator from (1/2/3/4): '))

num1 = int(input('First Number: '))
num2 = int(input('Second Number: '))

if operator == 1:
    print(f"{num1} + {num2} = {addition(num1, num2)}")
elif operator == 2:
    print(f"{num1} - {num2} = {subtraction(num1, num2)}")
elif operator == 3:
    print(f"{num1} * {num2} = {multiplication(num1, num2)}")
elif operator == 4:
    print(f"{num1} / {num2} = {division(num1, num2)}")
else:
    print('Can not Perform the Operation')





