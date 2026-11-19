nums = [5,9,4]
target = 8
result = []
def solve(index,total):
    if total == target:
        return True 
    elif index>=len(nums) or total>target:
        return False
    sum = total + nums[index]
    pick = solve(index + 1,sum)
    if pick == True:
        return pick
    sum = total
    not_pick = solve(index + 1,sum)
    return not_pick
ans = solve(0,0)
print(ans)