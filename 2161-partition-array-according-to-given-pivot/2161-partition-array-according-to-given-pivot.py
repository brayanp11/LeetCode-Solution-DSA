class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left, right = 0, len(nums) - 1
        res = [0] * len(nums)

        for num in nums:
            if num < pivot:
                res[left] = num
                left += 1

        for num in reversed(nums):
            if num > pivot:
                res[right] = num
                right -= 1

        while left <= right:
            res[left] = pivot
            left += 1

        return res