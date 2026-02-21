class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = curr = 0

        for num in nums:
            if num:
                curr += 1
                if max_ones < curr:
                    max_ones = curr
            else:
                curr = 0

        return max_ones