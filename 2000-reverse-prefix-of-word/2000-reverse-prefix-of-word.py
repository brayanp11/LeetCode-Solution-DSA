class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        k = word.find(ch)

        if k == -1:
            return word

        res = list(word)
        left, right = 0, k
        while left < right:
            res[left], res[right] = res[right], res[left]
            left += 1
            right -= 1

        return "".join(res)