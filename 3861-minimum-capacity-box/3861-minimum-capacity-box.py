class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        res = float("inf")
        for i in range(len(capacity)):
            if itemSize <= capacity[i]:
                res = min(res, capacity[i])

        try:
            return capacity.index(res)
        except:
            return -1