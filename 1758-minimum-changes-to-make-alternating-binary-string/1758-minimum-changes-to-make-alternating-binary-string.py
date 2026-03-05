class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        count = 0

        for i in range(n):
            expected = str(i % 2)

            if s[i] != expected:
                count += 1

        return min(count, n - count)