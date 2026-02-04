class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left, right = 0, 1
        n = len(nums)

        while n > right:
            if nums[left] == 0 and nums[right] == 0:
                right += 1
            elif nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
            elif nums[left] != 0 and nums[right] == 0:
                left += 1
            else:
                left += 1
                right += 1
        return nums