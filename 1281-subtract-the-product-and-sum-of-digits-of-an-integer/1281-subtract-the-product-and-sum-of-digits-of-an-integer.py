class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        p = 1
        s = 0

        while temp > 0:
            r = temp % 10
            temp //= 10
            p *= r
            s += r

        return p - s