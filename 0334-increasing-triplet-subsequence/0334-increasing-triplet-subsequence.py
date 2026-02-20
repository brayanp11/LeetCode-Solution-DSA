class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = nums[0]
        second = None

        for num in nums:
            if num <= first:
                first = num
            elif second is None or num <= second:
                second = num
            else:
                return True
        return False