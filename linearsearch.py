#IMPLEMENTS LINEAR SEARCH ALGORITHM USING LIST
def linearsearch(arr,search):
    for i in range(len(arr)):#iterates index of the array to access the elements of the array
        if arr[i]==search:#check whether the given search element matches with the element at 'i' index or not
            print(arr[i],"found at position",i)    
            break
    else:#returns element not found if the element is not found
        print(search," not found in the given array")
        
arr=list(map(int,input().split()))#initialising an array- take input from the user:enter input with giving space
search=int(input("enter element to search:"))#input from user to enetr an element to search in the given array
linearsearch(arr,search)#linear search function call with the parameters array and the search element
