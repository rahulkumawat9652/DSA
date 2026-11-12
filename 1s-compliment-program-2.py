x = [1,1,0,1]
index = 0
while index < len(x):
    if x[index] == 1:
        x[index] = 0
    else:
        x[index] = 1
    index += 1
print(x)