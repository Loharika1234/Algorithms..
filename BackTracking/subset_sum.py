def subsetsum(arr,target):
  result=[]
  current=[]
  def backtrack(index,total):
    if total==target:
      if total==target:
        result.append(current.copy())
        return 
    current.append(arr[index])
    backtrack(index+1,total+arr[index])
    current.pop()
    backtrack(index+1,total)
  backtrack(0,0)
  return result
arr=[2,3,5,6,8]
target=8
print(subsetsum(arr,target))
    
