def summ(a: str , b: str):
    return eval(f'{a} + {b}')

def sub(a: str, b: str):
    return eval(f'{a} - {b}')

def div(a: str, b: str):
    if a != '0' and b != '0':
        return eval(f'{a} / {b}')
    else:
        return 'На ноль делить нельзя!'
def mult(a: str, b: str):
    return eval(f'{a} * {b}')

