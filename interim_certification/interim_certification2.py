from utils import summ, sub, div, mult, validation_operation, validation_integer
answer = ''
while answer != '0':

    number1 = input('Введите первое число: ').strip()
    if validation_integer(number1) is False:
        print('Введите число корректно')
        number1 = input('Введите первое число : ').strip()

    operation = input('Операция? (+, -, *, /): ').strip()
    if validation_operation(operation) is False:
        print('Введите операцию корректно')
        operation = input('Операция? (+, -, *, /): ').strip()


    number2 = input('Введите второе число : ').strip()
    if validation_integer(number2) is False:
        print('Введите число корректно')
        number2 = input('Введите второе число : ').strip()


    if operation == '+':
        print(summ(float(number1), float(number2)))
    elif operation == '-':
        print(sub(float(number1), float(number2)))
    elif operation == '/':
        print(div(float(number1), float(number2)))
    elif operation == '*':
        print(mult(float(number1), float(number2)))

    answer = input('Хотите продолжить? (1 - Да, 0 - Нет) - ').strip()
    while answer != '0' and answer != '1':
        print('Введите ответ корректно! ')
        answer = input('Хотите продолжить? !(1 - Да, 0 - Нет)! - ').strip()
else:
    print('Конец')