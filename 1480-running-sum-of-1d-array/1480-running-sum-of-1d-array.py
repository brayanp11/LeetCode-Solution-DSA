class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefixSum = [0] * n
        prefixSum[0] = nums[0]

        for i in range(1, n):
            prefixSum[i] = nums[i] + prefixSum[i - 1]

        return prefixSum