class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            left, right = 0, len(word) - 1
            while left < right:
                if word[left] == word[right]:
                    left += 1
                    right -= 1
                else: break
            if left >= right:
                return word
        return ""