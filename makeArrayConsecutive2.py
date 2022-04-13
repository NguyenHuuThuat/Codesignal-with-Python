def solution(statues):
    add = 0
    n = len(statues)

    statues = bubbleSort(statues)

    for i in range(0, n-1):
        tmp_2 = statues[i+1] - statues[i]
        if tmp_2 > 1:
            add += (tmp_2 - 1)
    return add

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if arr[j+1] < arr[j]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    return arr
            
statues = [122,8, 1, 0, 4, 7,7,8,0,1,2,4,7,5,10,1,100]
print(bubbleSort(statues))