def basic_calculator():
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

basic_calculator()
