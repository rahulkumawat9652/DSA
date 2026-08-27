nums = [-3,4,3,2,-8,4]
n = len(nums)
maxi = float("-inf")
total = 0
for i in range(0,n):
    total = total + nums[i]
    maxi = max(maxi , total)
    if total < 0:
        total = 0
print(maxi)