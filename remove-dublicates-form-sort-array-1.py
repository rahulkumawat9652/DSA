nums = [1,2,2,3,3,4,5,5,6,7,7,8,8,9]
n = len(nums)
if n == 1:
    print(1)
i = 0
j = i+1
while j < n:
    if nums[j]!=nums[i]:
        i+=1
        nums[i],nums[j] = nums[j],nums[i]
    j+=1
print(nums[:i+1])