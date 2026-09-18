nums = [-1,0,1,2,2,-1,-4]
n = len(nums)
my_set = set()
target = 0
for i in range(0,n):
    for j in range(i+1,n):
        hash_set = set()
        for k in range(j+1,n):
            fourth = target - (nums[i] + nums[j] +nums[k])
            if fourth in hash_set:
                t = [nums[i],nums[j],nums[k],fourth]
                t.sort()
                my_set.add(tuple(t))
            hash_set.add(nums[k])
print(my_set)