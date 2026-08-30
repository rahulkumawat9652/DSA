nums = [5,10,-3,-1,-10,6]
n = len(nums)
result = [0]*n
posindex,negindex = 0,1
for i in range(0,n):
    if nums[i]>=0:
        result[posindex] = nums[i]
        posindex +=2
    else:
        result[negindex] = nums[i]
        negindex +=2
print(result)