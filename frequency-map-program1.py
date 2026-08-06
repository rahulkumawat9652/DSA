num = [1,2,3,4,5,6]
freq_map = dict()
for i in range(0,len(num)):
    if num[i] is freq_map:
        freq_map[num[i]] += 1
    else:
        freq_map[num[i]] = 1
print(freq_map)