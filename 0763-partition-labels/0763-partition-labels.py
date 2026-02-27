class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {char:i for i, char in enumerate(s)}

        start, end = 0, 0
        ans = []

        for i, char in enumerate(s):
            if last[char] > end:
                end = last[char]
            
            if i == end:
                ans.append(i - start + 1)
                start = end + 1

        return ans