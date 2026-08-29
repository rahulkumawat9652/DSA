nums = [1,99,101,98,2,5,3,100,1,2]
nums.sort()
n = len(nums)
count = 0
last_smaller = float("inf")
longest = 0
for i in range(0,n):
    num = nums[i]
    if num-1 == last_smaller:
        count+=1
        last_smaller = num
    elif num!=last_smaller:
        count = 1
        last_smaller = num
    longest = max(longest,count)
print(longest)