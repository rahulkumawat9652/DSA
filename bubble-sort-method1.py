nums = [1,3,4,5,67,8,7,3]
n = len(nums)
for i in range(n-2,-1,-1):
    for j in range(0,i+1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
print(nums)