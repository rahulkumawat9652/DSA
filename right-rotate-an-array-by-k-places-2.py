nums = [3,4,5,6,7,8,9]
n = len(nums)
k = int(input("Enter the number of places to rotate the array: "))
k = k % n
nums[:] = nums[n-k:] + nums[:n-k]
print(nums)