nums = [-2,3,5,7,-1,-5]
n = len(nums)
total = 0
maxi = float("-inf")
for i in range(0,n):
    total = 0
    for j in range(i ,n):
        total = total + nums[j]
        maxi = max(maxi,total)
print(maxi)