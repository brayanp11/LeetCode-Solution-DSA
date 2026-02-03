class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = [w for w in s.split(" ") if w != ""]
        left, right = 0, len(s_list) - 1

        while left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        return " ".join(s_list)