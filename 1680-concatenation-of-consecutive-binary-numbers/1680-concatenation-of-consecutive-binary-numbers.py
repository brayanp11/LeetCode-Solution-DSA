class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10**9 + 7
        res = 0
        lenght = 0

        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                lenght += 1

            res = ((res << lenght) | i) % mod

        return res