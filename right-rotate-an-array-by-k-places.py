nums = [3,4,5,6,7,8,9]
n = len(nums)
k = int(input("Enter the number of places to rotate the array: "));
rotations = k%n
for i in range(0,rotations):
    e = nums.pop()
    nums.insert(0,e)
print(nums)