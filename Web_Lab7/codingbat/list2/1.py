def count_evens(nums):
  return len(list(filter(lambda x: x % 2 == 0, nums)))