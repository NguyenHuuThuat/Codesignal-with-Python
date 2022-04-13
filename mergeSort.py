import math
def mergeSort(arr):
    mid = int((len(arr) + 1) / 2)
    arr = []
    arr_left = arr[0:mid]
    arr_left.append(math.inf)
    arr_right = arr[mid+1:]
    arr_right.append(math.inf)
    i = 1
    j = 1
    for i in range(0, len(arr)):
        if arr_left[i] <= arr_right[j]:
            arr.append(arr_left[i])
            i += 1
        else:
            arr.append(arr_right[j])
            j += 1
    return arr

statues = [122,8, 1, 0, 4, 7,7,8,0,1,2,4,7,5,10,1,100]
print(mergeSort(statues)) 