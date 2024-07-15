# take the input
number = int(input('Enter the number: '))


# main function
def fibonacci_generator():
    first_number = 0
    second_number = 1

    while True:
        yield first_number
        first_number, second_number = second_number, first_number + second_number


fib_gen = fibonacci_generator()

# output
for i in range(number):
    print(next(fib_gen))
