nums = [17,18,20,1,2,3,4,5,6,7,10]
n = len(nums)
target = 8
low = 0
high = n-1
while low <= high:
    mid = (low + high)//2
    if nums[mid] == target:
        print(True)
        break
    if nums[low] == nums[mid] == nums[high]:
        low += 1
        high -= 1
        continue
    if nums[mid] <= nums[high]:
        if nums[mid] <= target <= nums[high]:
            low = mid + 1
        else:
            high = mid - 1
    else:
        if nums[low] <= target <= nums[mid]:
            high = mid-1
        else:
            low = mid + 1
else:
    print(False)