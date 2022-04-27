def solution(n):
    h = int(n/60)
    m = n % 60
    h = str(h)
    m = str(m)
    sum = 0
    for i in range(0, len(h)):
        sum += int(h[i])
    for i in range(0, len(m)):
        sum += int(m[i])

    return sum
    

n = 240
print(solution(n))