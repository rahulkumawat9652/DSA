nums = [5,9,4]
target = 9
result = []
def solve(index,total,subset):
    if total == target:
        result.append(subset.copy())
        return
    elif index>=len(nums) or total>target:
        return
    subset.append(nums[index])
    sum = total + nums[index]
    solve(index + 1,sum,subset)
    e = subset.pop()
    sum -= e
    solve(index + 1,sum,subset)
solve(0,0,[])
print(result)