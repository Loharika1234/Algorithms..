#IMPLEMENTATION OF BINARY SEARCH ON LIST
#To implement binary search on given elements, first we have to arrange the elements in the sorted order.It is the compulsory step which makes the process of searching more optimised.
#In this we use mainly use 3 variables- low,mid,high
#initially low=0, high=len(arr)-1, and mid=(low+high)//2
#we divide the the gucen numbver of elements into half using mid and then we check whether the mid element matches with target element or not.
#if the element matches, we stop that iteration.
#else, we will continue the number of iterations on the next half by checking whether the target is less than or greater than the mid element.
#if it is lesser, we perform this iteration on the left side part of the list by making high as mid-1
#or else we make low as mid+1 if theb target element is greater than the target element.
#this continues until the element is found or it traverses all the elements in the list.

def binarysearch(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            print(target,"found at position",mid)
            break
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    else:
        print(target,"not found")
    
arr=list(map(int,input("enter elements in sorted order:").split()))
target=int(input("enter element to search:"))
binarysearch(arr,target)#function call
