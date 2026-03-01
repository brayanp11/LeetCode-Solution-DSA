class Solution:
    def minPartitions(self, n: str) -> int:
        n = set(n)
        if '9' in n: return 9
        return int(max(n))