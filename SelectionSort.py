def selectionSort(arr):
    min_tmp = 0
    for i in range(0, len(arr)):
        min_tmp = arr[i]
        for j in range(i+1, len(arr)):
            if min_tmp > arr[j]:
                min_tmp = arr[j]
        arr[j] = arr[i]
        arr[i] = min_tmp
    return arr

def slectSort(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(i+1 , n):
            if(arr[i] > arr[j]):
                tmp = arr[j]
                arr[j] = arr[i]
                arr[i] = tmp
    return arr
            
statues = [122,8, 1, 0, 4, 7,7,8,0,1,2,4,7,5,10,1,100]
print(slectSort(statues))

# arr = [100, 0, 10, 9, 120]
# print(selectionSort(arr))
