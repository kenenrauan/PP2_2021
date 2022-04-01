def centered_average(nums):
  return (sum(nums) - min(nums) - max(nums)) // (len(nums) - 2)