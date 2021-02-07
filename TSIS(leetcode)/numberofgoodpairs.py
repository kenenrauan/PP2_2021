class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        for x in range(0, len(nums) - 1): 
            for y in range(x + 1, len(nums)):
                if nums[x] == nums[y]:
                    ans += 1
        return ans