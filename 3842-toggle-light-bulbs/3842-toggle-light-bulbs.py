class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        seen = set()
        for bulb in bulbs:
            if bulb not in seen:
                seen.add(bulb)
            else:
                seen.remove(bulb)
        return sorted(list(seen))