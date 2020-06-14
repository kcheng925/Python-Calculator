op = input('Select an operation: \n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide \n 5. Exit \n')
op = op.lower()

if op == '1' or op == 'add':
    num1 = int(input('Input first number: '))
    num2 = int(input('Input second number: '))
    print(num1 + num2)

elif op == '2' or op == 'subtract':
    num1 = int(input('Input first number: '))
    num2 = int(input('Input second number: '))
    print(num1 - num2)

elif op == '3' or op == 'multiply':
    num1 = int(input('Input first number: '))
    num2 = int(input('Input second number: '))
    print(num1 * num2)

elif op == '4' or op == 'divide':
    num1 = int(input('Input first number: '))
    num2 = int(input('Input second number: '))
    if num2 == 0:
        print('Cannot divide by zero')
    else:
        print(num1 / num2)

elif op == '5' or op == 'exit':
    print('Goodbye!')