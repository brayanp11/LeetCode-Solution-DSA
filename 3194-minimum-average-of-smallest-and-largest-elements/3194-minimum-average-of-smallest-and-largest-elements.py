from collections import deque
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        nums = deque(nums)
        avg = 0
        res = []
        while nums:
            maxElement = nums.pop()
            minElement = nums.popleft()
            avg = (minElement + maxElement) / 2
            res.append(avg)
        return min(res)