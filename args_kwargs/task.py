# def addition(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result
#
# def arg_printer(a, b, *args):
#     print(f'a is {a}')
#     print(f'b is {b}')
#     print(f'args are {args}')
# arg_printer(3, 4, 5)
#
#
# def addition(a, b, *args, option=True):
#     result = 0
#     if option:
#         for i in args:
#             result += i
#         return a + b + result
#     return result
# print(addition(1, 7, 8, 9 , option= False))

def arg_printer(a, b, option=True, **kwargs):
    print(a, b)
    print(option)
    print(kwargs)
arg_printer(3, 4, param1=5, param2=6)