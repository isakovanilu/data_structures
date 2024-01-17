def basic_calculator():
    a = int(input('Enter a number1: '))
    b = int(input('Enter a number2: '))
    operation = input('Enter an arithmetic operations: like add, sub, mult, div ').lower().strip()

    if operation == 'add':
        result = a+b
    elif operation == 'sub':
        result = a-b
    elif operation == 'mult':
        result = a*b
    elif operation == 'div':
        result = a/b if b != 0 else 'denominator cannot be zero'
    else:
        print('invalid input')
    print('result: ', result)

basic_calculator()
