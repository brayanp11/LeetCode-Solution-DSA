class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        max_sum = 0
        while left < right:
            curr = nums[left] + nums[right]
            if max_sum < curr:
                max_sum = curr
            left += 1
            right -= 1
        return max_sum