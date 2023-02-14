from utils import summ, sub, div, mult
answer = 2
while answer != 0:
    operation = input('Операция ? (+, -, /, *) : ')
    number1 = int(input('Введите первое число : '))
    number2 = int(input('Введите второе число : '))
    if operation == '+':
        print(summ(number1, number2))
    elif operation == '-':
        print(sub(number1, number2))
    elif operation == '/':
        print(div(number1, number2))
    elif operation == '*':
        print(mult(number1, number2))
    else:
        print('Введите операцию корректно!')
        continue
    answer = int(input('Хотите продолжить? (1 - Да, 0 - Нет) - '))
else:
    print('Конец')