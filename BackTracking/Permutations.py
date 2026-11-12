def generate_permutations(arr):
  result=[]
  current=[]
  used=[False]*len(arr)
  def backtrack():
    if len(current)==len(arr):
      result.append(current.copy())
      return
    for i in range(len(arr)):
      if used[i]:
        continue
    current.append(arr[i])
    used[i]=True
    backtrack()
    current.pop()
    used[i]=False
  backtrack()
  return result
print(generate_permutations([1,2,3]))
