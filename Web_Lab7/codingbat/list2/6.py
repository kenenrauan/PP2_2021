def has22(nums):
  for i in range(1, len(nums)):
    if nums[i - 1] == nums[i] == 2: return True
  return False