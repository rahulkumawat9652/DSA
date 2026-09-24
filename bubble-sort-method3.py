num = [5, 7, 8, 4, 1, 6, 9, 2]
n = len(num)
for i in range(0, n-1):
    for j in range(i, n-1):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]
print(num)