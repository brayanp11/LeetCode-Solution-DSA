class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        left, right = 0, len(nums) - 1
        avg = 0
        res = []
        while left < right:
            maxElement = nums.pop()
            minElement = nums.pop(left)
            avg = (minElement + maxElement) / 2
            res.append(avg)
            right -= 2
        return min(res)