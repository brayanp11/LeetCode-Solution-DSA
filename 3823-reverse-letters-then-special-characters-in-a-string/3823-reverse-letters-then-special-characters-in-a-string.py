class Solution:
    def reverseByType(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalpha():
                left += 1
            while left < right and not s[right].isalpha():
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        left, right = 0, len(s) - 1
        while left < right:
            while left < right and s[left].isalpha():
                left += 1
            while left < right and s[right].isalpha():
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return "".join(s)