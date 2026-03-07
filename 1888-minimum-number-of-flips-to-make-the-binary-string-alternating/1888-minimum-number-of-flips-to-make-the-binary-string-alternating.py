class Solution:
    def minFlips(self, s: str) -> int:
        s2 = s + s

        n = len(s2)

        res = float("inf")
        ans1, ans2 = [], []

        count1, count2 = 0, 0

        for i in range(n):
            if i % 2 == 0:
                ans1.append("0")
                ans2.append("1")
            else:
                ans1.append("1")
                ans2.append("0")

        left = 0

        for right in range(n):
            if s2[right] != ans1[right]:
                count1 += 1
            if s2[right] != ans2[right]:
                count2 += 1

            if right - left  + 1 > len(s):
                if s2[left] != ans1[left]:
                    count1 -= 1
                if s2[left] != ans2[left]:
                    count2 -= 1
                left += 1

            if right - left  + 1 == len(s):
                res = min(res, count1, count2)

        return res