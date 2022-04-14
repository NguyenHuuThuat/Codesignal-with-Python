from os import TMP_MAX


def selectionSort(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
    return arr

def solution(a):
    index = []
    value = []
    for i in range(0, len(a)):
        if a[i] != -1:
            value.append(a[i])
            index.append(i)
    
    selectionSort(value)
    selectionSort(index)
    j = 0
    for i in index:
        a[i] = value[j]
        j += 1
    
    return a


a = [-1, 150, 190, 170, -1, -1, 160, 180]
sol = solution(a)

print(sol)


    
        