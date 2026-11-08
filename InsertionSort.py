def insertionsort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
arr=[5,8,6,3,1,9,6,3,4,7,56,3,1]
print("sorted array:",insertionsort(arr))
