a = [1,2,3,4,53,5,6,10,7]
n = len(a)
largest = float("-inf")
s_largest = float("-inf")
smallest = float("inf")
s_smallest = float("inf")
for i in range(n):
    if a[i] > largest:
        s_largest = largest
        largest = a[i]
    elif a[i] > s_largest:
        s_largest = a[i]
    if a[i] < smallest:
        s_smallest = smallest
        smallest = a[i]
    elif a[i] < s_smallest:
        s_smallest = a[i]
print([largest, smallest])
print([s_largest, s_smallest])