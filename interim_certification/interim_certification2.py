#https://gitlab.com/alexandrnaumov2911/linteh_28

from utils import summ, sub, div, mult, validation_2, validation_operation
answer = ''
while answer != '0':

    number1 = input('Введите первое число: ').strip()
    if validation_2(number1) is False:
        print('Введите число корректно')
        continue

    operation = input('Операция? (+, -, *, /): ').strip()
    if validation_operation(operation) is False:
        print('Введите операцию корректно')
        continue


    number2 = input('Введите второе число : ').strip()
    if validation_2(number2) is False:
        print('Введите число корректно')
        continue

    dict_operators = {
        '+' : summ,
        '-' : sub,
        '/' : div,
        '*' : mult
    }

    print(dict_operators.get(operation)(number1, number2))

    answer = input('Хотите продолжить? (1 - Да, 0 - Нет) - ').strip()
    while answer != '0' and answer != '1':
        print('Введите ответ корректно! ')
        answer = input('Хотите продолжить? !(1 - Да, 0 - Нет)! - ').strip()
else:
    print('Конец')