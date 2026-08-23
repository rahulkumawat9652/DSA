nums = [2,4,7,8,4,9,2,0,4]
n = len(nums)
target = int(input("Enter the target number: "))
for i in range(n):
    if nums[i] == target:
        print(i)
        break
else:
    print(-1)