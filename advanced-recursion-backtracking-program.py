result = []
n = 3
bracket = [""] * (2 * n)
def solve(ind,total,bracket,result):
    if ind >= len(bracket):
        if total == 0:
            result.append("".join(bracket))
        return
    if total>len(bracket)//2:
        return
    elif total < 0:
        return
    bracket[ind] = "("
    sum = total+1
    solve(ind+1,sum,bracket,result)
    if total > 0:
        bracket[ind] = ")"
        sum = total-1
        solve(ind+1,sum,bracket,result)
solve(0, 0, bracket, result)
print(result)