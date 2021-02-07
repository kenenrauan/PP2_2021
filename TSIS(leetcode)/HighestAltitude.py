class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxx = -99999
        sum = 0
        ans = [0]
        for x in gain :
            sum += x
            ans.append(sum)
        for x in ans:
            if x > maxx:
                maxx = x
        return maxx