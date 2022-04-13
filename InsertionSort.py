def insertionSort(arr):
    
    for i in range(0, len(arr)):
        last = arr[i]
        j = i

        while (j > 0) and (arr[j-1] > last):
            arr[j] = arr[j-1]
            j = j-1

        arr[j] = last
    return arr
arr = [100, 0, 10, 9, 120]
print(insertionSort(arr))