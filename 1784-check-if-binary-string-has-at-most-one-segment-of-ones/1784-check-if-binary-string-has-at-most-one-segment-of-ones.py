class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        count1 = Counter(s)
        count = 0
        for i in range(count1["1"]):
            if s[i] == "1":
                count += 1
        return count == count1["1"]