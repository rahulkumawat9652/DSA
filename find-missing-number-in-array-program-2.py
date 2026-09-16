nums = [0,1,2,3,4,5,6,7,8,9]
n = len(nums)
freq = {}
for i in range(0,n+1):
    freq[i]=0
for num in nums:
    freq[num]=1
for k,v in freq.items():
    if v == 0:
        print(k)