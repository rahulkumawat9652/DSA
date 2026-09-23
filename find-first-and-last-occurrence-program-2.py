nums = [1,1,1,2,2,2,4,4,5,5,6,6,6,6,7,8,10]
def lowerbound(nums,target):
    n = len(nums)
    lb = n
    low = 0
    high= n-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid] >= target:
            lb = mid
            high = mid-1
        else:
            low = mid +1
    return lb
def uperbound(nums,target):
    n = len(nums)
    ub = n
    low = 0
    high= n-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid] > target:
            ub = mid
            high = mid-1
        else:
            low = mid +1
    return ub
lb = lowerbound(nums,3)
ub = uperbound(nums,3)
print(lb,ub-1)