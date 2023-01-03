class Operations(int):

    def __init__(self, num:int):
        super().__init__()
        self.num = num

    def __add__(self, num2):
        return f'Происходит умножение {self.num * num2}'

    def __sub__(self, num2):
        return f'Происходит деление {self.num / num2}'

    def __mul__(self, num2):
        return f'Происходит вычитание {self.num - num2}'

    def __truediv__(self, num2):
        return f'Происходит сложение {self.num + num2}'

integer = int(input('Введите целое число - '))
number = Operations(integer)
print(number / 2)

