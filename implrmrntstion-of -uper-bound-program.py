nums = [1,1,1,2,2,2,4,4,5,5,6,6,6,6,7,8,10]
n = len(nums)
ub = n
target = 6
low = 0
high= n-1
while low <= high:
    mid = (low+high)//2
    if nums[mid] > target:
        ub = mid
        high = mid-1
    else:
        low = mid +1
print(ub)