class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        for num in nums:
            res += num
        return res % k
