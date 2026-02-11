class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        col = Counter(zip(*grid))

        count = 0
        for row in grid:
            count += col[tuple(row)]

        return count