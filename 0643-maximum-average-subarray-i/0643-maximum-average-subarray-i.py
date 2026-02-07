class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum_max = sum(nums[:k])
        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i - k]
            sum_max = max(sum_max, curr_sum)
        return sum_max / k