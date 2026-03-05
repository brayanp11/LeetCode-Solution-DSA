class Solution:
    def minOperations(self, s: str) -> int:
        ans1 = ["1"] * len(s)
        ans2 = ["0"] * len(s)

        count1, count2 = 0, 0

        for i in range(0, len(ans1), 2):
            ans1[i] = str(1 - int(ans1[i]))

        for i in range(0, len(ans2), 2):
            ans2[i] = str(1 - int(ans2[i]))

        for i in range(len(s)):
            if ans1[i] != s[i]:
                count1 += 1
            if ans2[i] != s[i]:
                count2 += 1
        
        return min(count1, count2)