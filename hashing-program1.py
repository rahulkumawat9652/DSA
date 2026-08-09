n = [1,2,3,4,5,1,4,6,7,8]
m = [1,4,6,3,8,9,]
hash_list = {}
for num in n:
    if num in hash_list:
        hash_list[num] += 1
    else:
        hash_list[num] = 1
for num in m:
    if num in hash_list:
        print(hash_list[num])
    else:
        print(0)