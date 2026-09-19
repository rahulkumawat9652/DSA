nums = [2,3,4,5,7,12,14,19]
def binarysearch(nums,target):
    n = len(nums)
    low = 0
    high = n-1
    while low <= high:
        mid = (low + high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid]<target:
            low = mid + 1
        else:
            high = mid -1
    return -1
target = 14
result = binarysearch(nums,target)
print("index ",result)