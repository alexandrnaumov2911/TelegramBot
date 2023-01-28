def ReName(dictionary: iter):
    result_list1 = list()
    while len(dictionary) > 0:
        x = dictionary.popitem()
        for i in range(len(x[1])):
             result_list1.append(x[1][i] + '@' + x[0])
    return result_list1
