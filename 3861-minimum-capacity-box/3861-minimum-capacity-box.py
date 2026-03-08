class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        res = -1
        for i in range(len(capacity)):
            if itemSize <= capacity[i]:
                if res == -1 or capacity[i] < capacity[res]:
                    res = i

        return res