class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}

        for num in arr:
            count[num] = 1 + count.get(num, 0)

        return len(set(count.values())) == len(count.values())