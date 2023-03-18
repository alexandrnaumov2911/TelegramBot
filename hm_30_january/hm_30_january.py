from datetime import datetime

def decorator(fn):

    def wrapper():
        print(f'start function - {fn.__name__}')
        start = datetime.now()
        fn()
        finish = datetime.now()
        print(finish - start)
        print('finish')

    return wrapper

@decorator
def long_func():
    x = 1
    for i in range(1_000_000):
        k = x ** i

long_func()