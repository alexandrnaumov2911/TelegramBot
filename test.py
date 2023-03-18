from numba import njit

@njit
def max_sequence(arr):
    if 0 in [1 if (arr[i] > 0) else 0 for i in arr]:
        summa = [sum(arr[s:i+1]) for i in range (len(arr)) for s in range(len(arr))]
        return max(summa)
    return sum(arr)
print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4,]))