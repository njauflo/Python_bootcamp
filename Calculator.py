operation = input ('Would you like to add/subtract/multiply/divide?').lower()
print(f'You chose {operation}.')
#ask for numbers, alert order matters for subtracting and dividing
if operation == 'subtract' or operation =='divide':
    print(f'You chose {operation}.')
    print('Please keep in mind that the order of your numbers matter.')
num1 =input ('What is the first number?')
num2 = input('What is the second number?')
print(f'First Number: {num1}')
print(f'Second Number: {num2}')    