import random


def basic_calculator():
    """Basic Calculator: Create a program that takes
    two numbers as inputs and performs basic arithmetic
    operations (addition, subtraction, multiplication, division).
    This introduces the concept of variables, user input,
    and basic arithmetic operations."""
    while True:
        a = int(input('Enter a number1: '))
        b = int(input('Enter a number2: '))
        operation = input(
            'Enter an arithmetic operations: like add/a, sub/s, mult/m, div/d  ').lower().strip()

        if operation in ['add', 'a']:
            result = a + b
        elif operation in ['sub', 's']:
            result = a - b
        elif operation in ['mult', 'm']:
            result = a * b
        elif operation in ['div', 'd']:
            result = a / b if b != 0 else 'denominator cannot be zero'
        else:
            print('invalid input')
        print('result: ', result)
        continue_calculation = input(
            "do you want to continue? (yes/y/no/n): ").lower().strip()
        if continue_calculation not in ['yes', 'y']:
            break

# basic_calculator()


def number_guessing():
    """
    Number Guessing Game: Develop a simple game where
    the program randomly selects a number, and the user has to guess it.
    Provide hints like "too high" or "too low."
    This will teach control structures (if-else statements) 
    and the use of random number generation.
    """

    rand_number = random.randint(1, 10)
    while True:
        guessed_number = int(input('Enter a number to guess: ').strip())
        if rand_number < guessed_number:
            print('Too high')
        elif rand_number > guessed_number:
            print('Too low')
        elif rand_number == guessed_number:
            print('You have guessed the number')
            break


# number_guessing()

def reverse_string(string):
    """
    String Reverser: Write a program that takes a string 
    input and prints its reverse. 
    This task will help in understanding strings and loops.

    Args:
        string (str): A string

    Returns:
        str: reversed string
    """
    if len(string) == 1:
        print(string)
        return string
    result = ''

    for s in string:
        print(s)
        result = s.strip() + result
    print(result)
    return result
    
# reverse_string("hell o")

def palindrome_checker(string):
    """
    Palindrome Checker: Create a Python program that checks if a given string
    is a palindrome (reads the same backward as forward). 
    This enhances understanding of strings, loops, and conditional statements.

    Args:
        string (str): A string

    Returns:
        bool: A result
    """
    if len(string) == 1:
        return string
    result = ''

    for s in string:
        result = s + result
    if string.lower().strip() == result.lower().strip():
        print('its palindrome')
        return True
    print('not a palindrome')
    return False

# palindrome_checker("ollo ")

def factorial_num(n):
    """
    Factorial Calculator: Implement a program that 
    calculates the factorial of a given number. 
    This can be done using both iteration (loops) and recursion, 
    providing insight into different approaches to problem-solving.


    Args:
        n (int): An integer number

    Returns:
        int: factorial value of the given number
    """

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_num(n - 1)

# print(factorial_num(5))
    
    
def temperature_converter():
    """
    Temperature Converter: Write a program that converts temperature 
    from Fahrenheit to Celsius and vice versa. 
    This introduces the concept of user input 
    and basic mathematical formulas in programming.

    Returns:
        str: A value for F or C
    """
    temp = int(input('Enter the Number: '))
    metric = input('Enter metric to convert: F/f or C/c: ')
    
    if metric.upper() == 'F':
        result = (temp * 9/5) + 32 
        return f'{int(result)} F'

    elif metric.upper() == 'C':
        result = (temp - 32)*5/9
        return f'{int(result)} C'

        
# print(temperature_converter())


def count_vowels(string_test):
    """
    Count Vowels in a String: Develop a program that counts 
    the number of vowels in a given string. 
    This will help in understanding string manipulation 
    and the use of loops and conditionals.

    Args:
        string_test (str): A string containg vowels

    Returns:
        int: total counts of vowels in the given string
    """

    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_cnt = 0
    for i in string_test:
        if i in vowels:
            vowels_cnt+=1
    return vowels_cnt

print(count_vowels('sometimes'))