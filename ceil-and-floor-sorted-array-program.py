nums = [3,4,4,6,8,9,9,10,18,19]
n = len(nums)
target = 5
floor = -1
ceil = -1
low = 0
high = n-1
while low <= high:
    mid = (low + high)//2
    if nums[mid] == target:
        print(nums[mid],nums[mid])
    elif nums[mid] > target:
        ceil = nums[mid]
        high = mid - 1
    else:
        floor = nums[mid]
        k=low = mid + 1
print(floor,ceil)