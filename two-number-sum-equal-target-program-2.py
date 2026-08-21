nums = [5,9,2,4,6,7,13,4]
n = len(nums)
hash_map = {}
target = int(input("enter number target = "))
for i in range(0,n):
    remaining = target - nums[i]
    if remaining in hash_map:
        print(hash_map[remaining],i)
    hash_map[nums[i]] = i