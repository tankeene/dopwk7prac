import math

# Addition
def add(a, b):
    return a + b

# Subtraction
def subtract(a, b):
    return a - b

# Multiplication
def multiply(a, b):
    return a * b

# Division
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    elif b != 0:
        return a / b
    else:
        pass

# Sine
def sine(angle_degrees):
    angle_radians = math.radians(angle_degrees)  # Convert angle to radians
    return math.sin(angle_radians)

# Cosine
def cosine(angle_degrees):
    angle_radians = math.radians(angle_degrees)  # Convert angle to radians
    return math.cos(angle_radians)

# Tangent
def tangent(angle_degrees):
    angle_radians = math.radians(angle_degrees)  # Convert angle to radians
    if math.cos(angle_radians) == 0:  # To avoid division by zero in tangent calculation
        return "Error! Tangent undefined."
    return math.tan(angle_radians)

# program entry point
while True:
    operation = '+'
    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('You have not typed a valid operator, please run the program again.')

    # Take input from user
    calc_again = 'N'

    # If user types N, say goodbye to user and end program
    if calc_again =='N' or calc_again == 'n':
        print("See you later.")
        break