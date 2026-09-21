nums = [1,2,3,3,3,3,5,5,5,5,7,7,8,8]
def lowerbound(nums,target):
    n = len(nums)
    lb = -1
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid] >= target:
            lb = mid
            high = mid-1
        else:
            low = mid+1
    return lb
def uperbound(nums,target):
    n = len(nums)
    ub = n
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid] > target:
            ub = mid
            high = mid-1
        else:
            low = mid+1
    return ub
lb = lowerbound(nums,5)
ub = uperbound(nums,5)
print(ub-lb)