nums = [5,9,4]
target = 9
result = []
def solve(index,total):
    if total == target:
        return 1
    elif index>=len(nums) or total>target:
        return 0
    sum = total + nums[index]
    pick = solve(index + 1,sum)
    sum = total
    not_pick = solve(index + 1,sum)
    return pick + not_pick
ans = solve(0,0)
print(ans)