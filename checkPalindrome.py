import math

def solution(inputString):
    n = len(inputString)
    mid = math.floor(n/2)
    count = 0
    if n == 1:
        return True
    for i in range(0, mid):
        if inputString[i] == inputString[n-i-1]:
            count += 1
    if count == mid:
        return True
    else:
        return False  

if __name__ == '__main__':
    inputString = 'aabaa'
    sol = solution(inputString)
    print(sol)
        
            

    
