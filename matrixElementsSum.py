import numpy as np

def solution(matrix):
    row = len(matrix)
    col = len(matrix[0])
    # b = matrix.shape
    sum = 0
    
    for i in range(0, row):
        for j in range(0, col):
            if matrix[i][j] == 0:
                if i < row -1:
                    matrix[i+1][j] = 0
            else:
                sum += matrix[i][j]
    return sum


a = [[0, 1, 1, 2], 
     [0, 5, 0, 0], 
     [2, 0, 3, 3]]
p = solution(a)
print(p)

