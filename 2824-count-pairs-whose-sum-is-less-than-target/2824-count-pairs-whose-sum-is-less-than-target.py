class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, 1
        count = 0
        while left < n:
            while right < n:
                if nums[left] + nums[right] < target:
                    count += 1
                right += 1
            left += 1
            right = left + 1
        return count