class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) - 1
        res = list(s)
        vowels = set("aeiouAEIOU")

        while left < right:
            while left < right and res[left] not in vowels:
                left += 1
            while left < right and res[right] not in vowels:
                right -= 1
            if left < right:
                res[left], res[right] = res[right], res[left]
                left += 1
                right -= 1
                
        return ''.join(res)