class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        globalans = 0
        localans1 = 1
        localans2 = 0
        m = n
        while n != 0:
            localans1 *= n%10
            n = n // 10
        while m != 0:
            localans2 += m%10
            m = m // 10
        globalans = localans1 - localans2
        return globalans