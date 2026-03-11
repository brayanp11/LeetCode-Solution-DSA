class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        count0, count1 = 0, 0
        res = n
        s2 = s + s
        for i in range(n * 2):
            expected0 = '0' if i % 2 == 0 else '1'

            if s2[i] != expected0:
                count0 += 1
            
            if i >= n:
                left = i - n
                exp_left = '0' if left % 2 == 0 else '1'
                if s2[left] != exp_left:
                    count0 -= 1
            
            if i >= n - 1:
                count1 = n - count0
                res = min (res, min(count0, count1))

        return res