def solution(inputArray):
    result = []
    # find len max
    max_tmp = len(inputArray[0])
    for i in range(1, len(inputArray)):
        if len(inputArray[i]) > max_tmp:
            max_tmp = len(inputArray[i])
    
    for j in range(0, len(inputArray)):
        if len(inputArray[j]) == max_tmp:
            result.append(inputArray[j])
    return result








inputArray = ["aba", "aa", "ad", "vcd", "aba"]
print(solution(inputArray))
