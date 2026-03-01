class Solution:
    def minPartitions(self, n: str) -> int:
        n = set(n)
        cnt = float("-inf")
        for num in n:
            cnt = max(cnt, int(num))
            if cnt == 9: return cnt
        return cnt