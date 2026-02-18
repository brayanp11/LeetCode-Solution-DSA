class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")

        left, right = 0, len(s) - 1

        res = list(s)

        while left < right:
            while left < right and res[left] not in vowels:
                left += 1
            while left < right and res[right] not in vowels:
                right -= 1

            res[left], res[right] = res[right], res[left]

            left += 1
            right -= 1

        return "".join(res)