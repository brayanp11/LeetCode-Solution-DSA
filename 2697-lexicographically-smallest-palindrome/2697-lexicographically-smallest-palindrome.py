class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                min_letter = min(s[right], s[left])
                s[left], s[right] = min_letter, min_letter
            left += 1
            right -= 1
        return "".join(s)