#BUBBLESORT IMPLEMENTATION ON  THE GIVEN LIST OF NUMBERS..
#this is the bubble sorting algorithm to arrange numbers in ascending order..(small to big)
def bubblesort1(arr):
    n=len(arr)
    for i in  range(len(arr)):
        swapped=False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
    return arr
#this is the bubble sorting algorithm to arrange numbers in descending order..(big to small)
def bubblesort2(arr):
    n=len(arr)
    for i in  range(len(arr)):
        swapped=False
        for j in range(n-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
    return arr

nums=list(map(int,input("enter the numbers into list:").split()))
print(bubblesort1(nums)," --->> this is ascending order of the given array...")
print(bubblesort2(nums)," --->> this is descending order of the given array...")
