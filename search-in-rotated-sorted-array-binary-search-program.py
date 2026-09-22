nums = [17,18,20,1,2,3,4,5,6,7,10]
n = len(nums)
target = 6
low = 0
high = n-1
while low <= high:
    mid = (low + high)//2
    if nums[mid] == target:
        print(mid)
        break
    if nums[mid] <= nums[high]:
        if nums[mid] <= target <= nums[high]:
            low = mid+1
        else:
            high = mid-1
    else:
        if nums[low]<=target<=nums[high]:
            high = mid-1
        else:
            low = mid + 1
print("number not found")