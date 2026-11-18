nums = [5,9,4]
target = 9
result = []
def solve(index,total,subset):
    if total == target:
        result.append(subset.copy())
        return True 
    elif index>=len(nums) or total>target:
        return False
    subset.append(nums[index])
    sum = total + nums[index]
    pick = solve(index + 1,sum,subset)
    if pick == True:
        return pick
    e = subset.pop()
    sum = total
    not_pick = solve(index + 1,sum,subset)
    return not_pick
ans = solve(0,0,[])
print(ans)