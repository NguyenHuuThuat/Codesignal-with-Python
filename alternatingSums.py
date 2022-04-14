import numpy as np

def solution(a):
    arr_1 = []
    arr_2 = []
    arr = []
    for i in range(0, len(a)):
        if (i % 2) == 0:
            arr_1.append(a[i])
        else:
            arr_2.append(a[i])
    
    s1 = np.sum(arr_1)
    arr.append(s1)
    s2 = np.sum(arr_2)
    arr.append(s2)

    return arr


a = [50, 60, 60, 45, 70]
sol = solution(a)
print(sol)

