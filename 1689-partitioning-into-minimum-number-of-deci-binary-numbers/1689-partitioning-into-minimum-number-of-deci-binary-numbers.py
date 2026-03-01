class Solution:
    def minPartitions(self, n: str) -> int:
        cnt = float("-inf")
        for num in n:
            cnt = max(cnt, int(num))
        return cnt