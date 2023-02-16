from utils import summ, sub, div, mult
answer = ''
while answer != '0':

    number1 = input('Введите первое число : ').strip()
    while number1.isdigit() is False:
        print('Введите число корректно!')
        number1 = input('Введите первое число : ').strip()


    operation = input('Операция? (+, -, *, /): ').strip()
    while (operation != '+') and (operation != '-') and (operation != '/') and (operation != '*'):
        print('Введите операцию корректно')
        operation = input('Операция? (+, -, *, /): ').strip()


    number2 = input('Введите второе число : ').strip()
    while number2.isdigit() is False:
        print('Введите число корректно!')
        number2 = input('Введите второе число : ').strip()

    if operation == '+':
        print(summ(number1, number2))
    elif operation == '-':
        print(sub(number1, number2))
    elif operation == '/':
        print(div(number1, number2))
    elif operation == '*':
        print(mult(number1, number2))

    answer = input('Хотите продолжить? (1 - Да, 0 - Нет) - ').strip()
    while answer != '0' and answer != '1':
        print('Введите ответ корректно! ')
        answer = input('Хотите продолжить? !(1 - Да, 0 - Нет)! - ').strip()
else:
    print('Конец')