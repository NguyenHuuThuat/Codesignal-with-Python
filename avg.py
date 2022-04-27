def avg(*nums):
    n = len(nums)
    sum = 0
    for i in range(0, n):
        sum += nums[i]
    

    return sum/n


nums = 1, 2, 3 
print(avg(*nums))