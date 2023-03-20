def next_bigger(n):
    list1 = []
    n = str(n)
    for i in range(len(n), 0, -1):
        print(i)
        start = n
        end = start[i:]
        print(end)
        start = start[:i-2] + start[i-2:i+1][::-1]
        print(start)
    # if len(list1) != 0:
    #     return min(list1)
    # return -1
print(next_bigger(2017))
