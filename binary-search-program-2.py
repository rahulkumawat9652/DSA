nums = [2,3,4,5,7,12,14,19]
n = len(nums)
def binarysearch(nums,low,high):
    if low>high:
        return -1
    mid = (low + high)//2
    if nums[mid] == target:
        return mid
    elif nums[mid]<target:
        return binarysearch(nums,mid+1,high)
    else:
        return binarysearch(nums,low,mid-1)
target = 14
result = binarysearch(nums,0,n-1)
print(result)