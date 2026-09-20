nums = [1,2,3,3,3,3,5,5,5,5,7,7,7,8]
n = len(nums)
target = 4
first = -1
last = -1
for i in range(0,n):
    if nums[i] == target:
        if first == -1:
            first = i
        last = i
if first == -1:
    print("number not found")
else:
    print(last-first+1)