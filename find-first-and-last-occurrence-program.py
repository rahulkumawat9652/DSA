nums = [1,2,3,3,3,3,4,4,6,8,9,9,10]
n = len(nums)
target = 3
first = -1
last = -1
for i in range(0,n):
    if nums[i] == target:
        if first == -1:
            first = i
        last = i
print(first,last)