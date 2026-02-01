class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [0] * len(boxes)

        ball, moves = 0, 0
        for i in range(len(boxes)):
            res[i] = ball + moves
            moves += ball
            ball += int(boxes[i])

        ball, moves = 0, 0
        for i in reversed(range(len(boxes))):
            res[i] += ball + moves
            moves += ball
            ball += int(boxes[i])

        return res