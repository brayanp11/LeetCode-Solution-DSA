class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(2 ,n):
            if nums[i - 2] == 0:
                nums[i] = nums[i] ^ 1
                nums[i - 1] = nums[i - 1] ^ 1
                nums[i - 2] = nums[i - 2] ^ 1
                count += 1
        if sum(nums) == n:
            return count
        return -1