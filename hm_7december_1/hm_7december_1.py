def calc(x: int, op: str, y: int):
    if op == '+':
        return x+y
    elif op == '-':
        return x-y
    elif op == '*':
        return x*y
    elif op == '/':
        return x/y
integer_1 = int(input('Введите первое число '))
integer_2 = int(input('Введите второе число '))
operation = input('Введите операцию ')
print(calc(integer_1, operation, integer_2))
