class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        res = []
        for word in s:
            left, right = 0, len(word) - 1
            curr = [""] * len(word)
            while left <= right:
                curr[left], curr[right] = word[right], word[left]
                left += 1
                right -= 1
            res.append("".join(curr))
        return " ".join(res)
