nums = [5,7,9]
result = []
def func(ind,subset):
    if ind >= len(nums):
        result.append(subset.copy())
        return
    subset.append(nums[ind])
    func(ind + 1,subset)
    subset.pop()
    func(ind + 1,subset)
func(0, [])
print(result)