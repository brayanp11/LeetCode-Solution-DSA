class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        res = list(s)
        left, right = 0, k - 1

        while left < right:
            res[left], res[right] = res[right], res[left]
            left += 1
            right -= 1

        return "".join(res)