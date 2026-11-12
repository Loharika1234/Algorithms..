def combination_sum_Algo(candidates,target):
  result=[]
  current=[]
  candidates=sorted(set(candidates))
  def backtrack(start,remaining):
    if remaining==0:
      result.append(current.copy())
      return
    for i in range(start,len(candidates)):
      value=candidates[i]
      if value>remaining:
        break
      current.appen(value)
      backtrack(i,remaining - value)
      current.pop()
  backtrack(0,target)
  return result
candidates=[2,3,6,7]
target=7
print(combination_sum(candidates,target))
