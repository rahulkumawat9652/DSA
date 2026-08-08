n = [1,2,3,4,5,1,4,6,7,8]
m = [1,4,6,3,8,9,]
hash_list = [0]*11
for num in n:
    hash_list[num] += 1
for num in m:
    if num<1 or num>10:
        print(0)
    else:
        print(hash_list[num])