nums = [1,2,0,3,0,4,5,0,6,7,7,0,8,9]
n = len(nums)
if len(nums) == 1:
    print(nums)
i = 0
while i < len(nums):
    if nums[i]==0:
        break
    i+=1
if i == len(nums):
    print(nums)
j = i+1
while j < len(nums):
    if nums[j]!=0:
        nums[i],nums[j]=nums[j],nums[i]
        i+=1
    j+=1
print(nums)