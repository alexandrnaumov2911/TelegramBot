"""""
 Написать функцию isPrime, которая принимает число и возвращает простое число или нет
"""""

def isPrime(num):
    if num > 1:
        for i in range(2, num): # Взял такой диапазон для того чтобы проверить, делится ли число на что-то кроме себя и 1, если да - число простое
            if num%i == 0:
                return False
        return True
    else:
        return False
number = int(input())
print(isPrime(number))