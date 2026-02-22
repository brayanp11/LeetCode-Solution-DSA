class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        count = 0
        for num in nums:
            for num2 in nums:
                if num > num2:
                    count += 1
            res.append(count)
            count = 0

        return res