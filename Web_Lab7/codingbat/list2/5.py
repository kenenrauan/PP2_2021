def sum67(nums):
  flag = True
  sm = 0
  for x in nums:
    if x == 6:
      flag = False
    if flag:
      sm += x
    elif x == 7:
      flag = True
  return sm