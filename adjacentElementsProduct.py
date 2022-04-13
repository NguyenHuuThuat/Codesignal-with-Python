import numpy as np
def solution(inputArray):
    result = []

    for i in range(0, len(inputArray) - 1):
        result.append(inputArray[i]*inputArray[i+1])
    return np.max(result)


inputArray = [3, 6, -2, -5, 7, 3]
print(solution(inputArray))