class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        res = []
        for num in candies:
            if extraCandies + num >= max_candies:
                res.append(True)
            else:
                res.append(False)
        return res