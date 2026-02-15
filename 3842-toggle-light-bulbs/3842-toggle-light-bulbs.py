class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        is_on = [False] * 101
        for bulb in bulbs:
            is_on[bulb] = not is_on[bulb]
        return [i for i in range(1, 101) if is_on[i]]