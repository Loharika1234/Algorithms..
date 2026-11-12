def generate_subsets(arr):
  result=[]
  current=[]
  def backtrack(index):
    if index == len(arr):
      result.append(current.copy())
      return
    #choice 1:include current element
    current.append?(arr[index])
    backtrack(index+1)
    current.pop()
    backtrack(index+1)
  backtrack(0)
  return result
arr=[1,2,3]
generate_subsets(arr)
