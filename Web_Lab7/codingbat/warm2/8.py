def array123(nums):
  nums = map(str, nums)
  return ''.join(nums).count('123') > 0