def selectionSort(arr):
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
    return arr
                



def solution(a, b):
    count = 0
    len_max = len(a)


    for i in range(0, len_max):
        if a[i] != b[i]:
            count += 1       
    if selectionSort(a) == selectionSort(b) and count <= 2:
        return True
    else:
        return False



a = [4, 6, 3]
b = [3, 4, 6]
print(solution(a, b))

