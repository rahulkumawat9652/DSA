nums = [1,2,3,4,5,6,7,8,9]
def reverse(nums,left,right):
    while left<right:
        nums[left],nums[right] = nums[right],nums[left]
        left += 1
        right -= 1
n = len(nums)
reverse(nums,0,n-1)
print(nums)