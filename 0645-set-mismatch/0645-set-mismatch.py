class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ideal = n * (n + 1) // 2
        real = sum(nums)
        diff = sum(set(nums))
        missing = ideal - diff
        repeated = real - diff
        return [repeated, missing]