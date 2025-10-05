def twosum():
    nums = [2, 11, 7, 15]
    target = 9

    n = len(nums)
    for i in range(n):  
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

print(twosum()) 
