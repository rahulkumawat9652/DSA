nums = [1,3,4,5,6,7,9,10,19,20]
n = len(nums)
ib = n
target = 6
low = 0
high= n-1
while low <= high:
    mid = (low+high)//2
    if nums[mid] >= target:
        ib = mid
        high = mid-1
    else:
        low = mid +1
print(ib)