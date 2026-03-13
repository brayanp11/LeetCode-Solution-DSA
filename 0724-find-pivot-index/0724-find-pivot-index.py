class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        left_total = 0

        for i in range(len(nums)):
            right_total = totalSum - nums[i] - left_total

            if left_total == right_total:
                return i

            left_total += nums[i]
            
        return -1