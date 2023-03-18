print('exercise №1')

string = input().split(' ')
print(*list([string.count(elem) for elem in input().split(' ')]))
