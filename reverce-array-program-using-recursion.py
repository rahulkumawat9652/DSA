def func(nums,left,right):
    if left >= right:
        return
    arr[left],arr[right] = arr[right],arr[left]
    func(arr,left + 1,right - 1)
def reverse_array(nums,l,r):
    func(nums,l,r)
    return nums
arr = [1,2,3,4,5]
print(reverse_array(arr,0,len(arr)-1))  