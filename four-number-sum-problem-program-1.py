arr = [-1,0,1,2,2,-1,-4]
n = len(arr)
my_set = set()
for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            for l in range(k+1,n):
                total = arr[i] + arr[j] + arr[k] + arr[l]
                if total == 0:
                    temp = [arr[i], arr[j], arr[k], arr[l]]
                    temp.sort()
                    my_set.add(tuple(temp))
result = []
for ans in my_set:
    result.append(list(ans))
print(result)