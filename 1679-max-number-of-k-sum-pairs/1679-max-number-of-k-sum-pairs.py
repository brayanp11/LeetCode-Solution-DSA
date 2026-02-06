class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        count, add = 0, 0
        nums.sort()
        while left < right:
            add = nums[left] + nums[right]
            if add == k:
                count += 1
                left += 1
                right -= 1
            elif add < k:
                left += 1
            else:
                right -=1
        return count