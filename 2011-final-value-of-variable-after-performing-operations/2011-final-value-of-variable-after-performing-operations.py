class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x_values = {"X++":1, "++X":1, "X--":-1, "--X":-1}
        res = 0
        for op in operations:
            res += x_values[op]
        return res