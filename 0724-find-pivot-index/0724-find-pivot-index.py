class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ans = {}

        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            ans[i] = prefix_sum - nums[i]

        diff, pivot = 0, float('inf')
        suffix_sum = 0
        for i in range(len(nums) - 1, -1, -1):
            suffix_sum += nums[i]
            diff = suffix_sum - nums[i]

            if diff == ans[i]:
                pivot = min(pivot, i)

            if i == 0 and pivot < len(nums):
                return pivot
            
        return -1