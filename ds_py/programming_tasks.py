import random

def basic_calculator():
    """Basic Calculator: Create a program that takes two numbers as inputs and performs basic arithmetic operations (addition, subtraction, multiplication, division). This introduces the concept of variables, user input, and basic arithmetic operations."""
    while True:
        a = int(input('Enter a number1: '))
        b = int(input('Enter a number2: '))
        operation = input('Enter an arithmetic operations: like add/a, sub/s, mult/m, div/d  ').lower().strip()

        if operation in ['add', 'a']:
            result = a+b
        elif operation in ['sub', 's']:
            result = a-b
        elif operation in ['mult', 'm']:
            result = a*b
        elif operation in ['div', 'd']:
            result = a/b if b != 0 else 'denominator cannot be zero'
        else:
            print('invalid input')
        print('result: ', result)
        continue_calculation = input("do you want to continue? (yes/y/no/n): ").lower().strip()
        if continue_calculation not in ['yes', 'y']:
            break

# basic_calculator()

def number_guessing():
    rand_number = random.randint(1, 3)
    while True:
        print('rand_number', rand_number)
        guessed_number = int(input('Enter a number to guess: '))
        if rand_number < guessed_number:
            print('Too high')
        elif rand_number > guessed_number:
            print('Too low')
        elif rand_number == guessed_number:
            print('You have guessed the number')
            break
    
number_guessing()    
