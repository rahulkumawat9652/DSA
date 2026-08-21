nums = [5,9,1,2,3,15,6,6]
n = len(nums)
target = int(input("enter number target = "))
for i in range(0,n-1):
    for j in range(i+1,n):
        if nums[i]+nums[j] == target:
            print(nums[i],nums[j])
