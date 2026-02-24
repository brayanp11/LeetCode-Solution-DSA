class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)

        left, right = 0, n - 1
        res = [pivot] * n

        for i in range(n):
            if nums[i] < pivot:
                res[left] = nums[i]
                left += 1

            j = n - 1 - i
            if nums[j] > pivot:
                res[right] = nums[j]
                right -= 1
        return res