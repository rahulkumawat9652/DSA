num = [1,2,3,4,5,6]
freq_map = dict()
n = len(num)
for i in range(0,n):
    freq_map[num[i]] = freq_map.get(num[i],0) + 1
print(freq_map)