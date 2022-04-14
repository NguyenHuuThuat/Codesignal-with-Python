def solution(n):
    n = str(n)
    mid = int(len(n)/2)
    mid_ = mid -1
    n_left = n[0:mid]
    n_right = n[mid:]
    
    sum_l = 0
    sum_r = 0

    for i in range(0, mid):
        sum_l += int(n_left[i])

        sum_r += int(n_right[i])

    if sum_l == sum_r:
        return True
    else:
        return False






a = str(1230)
sol = solution(a)
print(sol)