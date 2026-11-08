def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[-1]
    left=[]
    right=[]
    for i in range(len(arr)-1):
        if arr[i]<=pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quicksort(left)+[pivot]+quicksort(right)
arr=[5,9,2,6,9,4,6,9,7,2,8,7,8]
print("sorted array:",quicksort(arr))
