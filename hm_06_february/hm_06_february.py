"""
Реализовать программу, которая рассчитывает площадь и периметр прямоугольника и обработать все возможное ошибки с помощью try..except.
"""
def square_and_perimeter(length: int, width: int):
    try:
        square = length * width
        perimeter = (length + width) * 2
        return f' Площадь - {square}, Периметр - {perimeter}'
    except Exception as err:
        print(f'Ошибка!, {err}')
print(square_and_perimeter(7, 4))
