nums = [17,18,20,1,2,3,4,5,6,7,10]
n = len(nums)
mini = float("inf")
for i in range(0,n):
    mini = min(mini,nums[i])
print(mini)