def sum13(nums):
  s = 0
  for i in range(len(nums)):
    if nums[i] != 13 and not (i and nums[i - 1] == 13): s += nums[i]
  return s