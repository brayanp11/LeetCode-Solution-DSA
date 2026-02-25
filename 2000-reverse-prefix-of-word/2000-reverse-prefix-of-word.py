class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        k = 0
        res = list(word)
        for i, c in enumerate(word):
            if c == ch:
                k = i
                break
        left, right = 0, k
        while left < right:
            res[left], res[right] = res[right], res[left]
            left += 1
            right -= 1

        return "".join(res)